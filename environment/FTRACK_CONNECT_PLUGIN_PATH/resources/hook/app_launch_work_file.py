import os
import re
import subprocess
import shutil
import operator

import ftrack
import ftrack_api
from bumpybox_environment import utils


def version_get(string, prefix, suffix=None):
    """ Extract version information from filenames.
    Code from Foundry"s nukescripts.version_get()
    """

    if string is None:
        raise ValueError("Empty version string - no match")

    regex = "." + prefix + "\d+"
    matches = re.findall(regex, string, re.IGNORECASE)
    if not len(matches):
        msg = "No " + prefix + " found in \"" + string + "\""
        raise ValueError(msg)
    return (matches[-1:][0][1], re.search("\d+", matches[-1:][0]).group())


def get_task_data(event):

    data = event["data"]
    identifier = event["data"]["application"]["identifier"]
    session = ftrack_api.Session()
    task = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )

    # DJV View, files get selected by the user.
    if identifier.startswith("djvview"):
        return

    # RV
    if identifier.startswith("rv"):
        return

    app_id = None

    # Nuke applications.
    if identifier.startswith("nuke"):
        app_id = "nuke"
    if identifier.startswith("nukex"):
        app_id = "nuke"
    if identifier.startswith("nuke_studio"):
        app_id = "nukestudio"

    # Maya
    if identifier.startswith("maya"):
        app_id = "maya"

    # Return if application is not recognized.
    if not app_id:
        msg = '{0} - Application is not recognized to open a file: "{1}"'
        print msg.format(__file__, identifier)
        return

    work_file = utils.get_work_file(session, task, app_id, 1)

    # Find all work files and categorize by version.
    files = {}
    work_file_head = work_file.split("".join(version_get(work_file, "v")))[0]
    if os.path.exists(os.path.dirname(work_file)):
        for f in os.listdir(os.path.dirname(work_file)):

            # If the file extension doesn't match, we'll ignore the file.
            if os.path.splitext(f)[1] != os.path.splitext(work_file)[1]:
                continue

            try:
                version = version_get(f, "v")[1]
                value = files.get(version, [])
                file_path = os.path.abspath(
                    os.path.join(os.path.dirname(work_file), f)
                ).replace("\\", "/")
                f_head = file_path.split("v" + version)[0]
                # Only compare against the head because user can have notations
                # after version number.
                if f_head == work_file_head:
                    value.append(file_path)
                    files[version] = value
            except ValueError:
                pass

    # Determine highest version files
    if files:
        work_file = max(files[max(files.keys())], key=os.path.getctime)

    # Get latest published source file
    components = session.query(
        "select version.version from Component where version.task.id is "
        "\"{0}\" and version.asset.type.short is \"source\"".format(task["id"])
    )

    latest_component = {"version": {"version": 0}}
    for component in components:
        version = component["version"]["version"]
        if version > latest_component["version"]["version"]:
            latest_component = component

    locations = {}
    for location in session.query("select id from Location"):
        locations[location["id"]] = location

    location_id = max(
        component.get_availability().iteritems(),
        key=operator.itemgetter(1)
    )[0]
    file_path = locations[location_id].get_resource_identifier(
        component
    )

    # If no work file is present, copy published file.
    # If work file is present, check if published source is of newer date then
    # copy across with a higher version.
    if not os.path.exists(work_file):
        if not os.path.exists(os.path.dirname(work_file)):
            os.makedirs(os.path.dirname(work_file))

        shutil.copy(file_path, work_file)
    else:
        if os.path.getmtime(file_path) > os.path.getmtime(work_file):
            work_file = utils.get_work_file(
                session, task, app_id, int(version_get(work_file, "v")[1]) + 1
            )
            shutil.copy(file_path, work_file)

    # If no work file exists, create a work file
    if not os.path.exists(work_file):

        if not os.path.exists(os.path.dirname(work_file)):
            os.makedirs(os.path.dirname(work_file))

        # Call Nuke terminal to create an empty work file
        if app_id == "nuke":
            subprocess.call([
                event["data"]["application"]["path"],
                "-i",
                "-t",
                os.path.abspath(
                    os.path.join(
                        os.path.dirname(__file__), "..", "nuke_save.py"
                    )
                ),
                work_file
            ])

        # Call Mayapy terminal to create an empty work file
        if app_id == "maya":
            subprocess.call(
                [
                    os.path.join(
                        os.path.dirname(
                            event["data"]["application"]["path"]
                        ),
                        "mayapy.exe"
                    ),
                    os.path.abspath(
                        os.path.join(
                            os.path.dirname(__file__), "..", "maya_save.py"
                        )
                    ),
                    work_file
                ]
            )

    # Get latest version from Ftrack publishes
    versions = session.query(
        "select version from AssetVersion where task.id is \"{0}\" and "
        "asset.type.short is \"source\"".format(task["id"])
    )

    latest_version = int(version_get(work_file, "v")[1])
    for v in versions:
        if latest_version < int(v["version"]):
            latest_version = int(v["version"])

    # Create latest version from work file if they are different versions
    latest_file = utils.get_work_file(session, task, app_id, latest_version)

    if not os.path.exists(latest_file):
        shutil.copy(work_file, latest_file)
        work_file = latest_file

    # Ask user what to open
    output = subprocess.check_output([
        "python",
        os.path.abspath(
            os.path.join(
                os.path.dirname(__file__), "..", "open_work_file.py"
            )
        ),
        work_file
    ])
    output_file = output.replace("\\", "/").splitlines()[0]

    # Only add the work file to the command if the user didn't cancel
    if os.path.exists(output_file):
        if app_id == "maya":
            data["command"].append("-file")

        data["command"].append(output_file)
    else:
        data["command"] = ""

    return data


def modify_application_launch(event):
    """Modify the application launch command with potential files to open"""

    data = event["data"]
    selection = event["data"]["context"]["selection"]

    if not selection:
        return

    entityType = selection[0]["entityType"]

    # task based actions
    if entityType == "task":
        data = get_task_data(event)

    return data


def register(registry, **kw):
    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.EVENT_HANDLERS:
        # Exit to avoid registering this plugin again.
        return

    subscription = "topic=ftrack.connect.application.launch"
    ftrack.EVENT_HUB.subscribe(subscription, modify_application_launch)
