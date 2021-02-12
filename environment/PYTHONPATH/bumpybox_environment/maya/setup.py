import os
import getpass

import pymel.core as pc

from avalon import api, io
from avalon.maya import commands
from pypeapp import Anatomy
from pype import lib, hosts


def lighting_setup():
    host = api.registered_host()

    # Setup file.
    path = r"Y:/my_petsaurus/work/lighting/lighting_setup.ma"
    pc.openFile(path, force=True)

    commands.reset_frame_range()

    lib.BuildWorkfile().process()

    # Try to assign "lookMain" to all container mesh nodes.
    for container in host.ls():
        members = []
        for member in pc.PyNode(container["objectName"]).members():
            if member.nodeType() != "transform":
                continue

            shape = member.getShape()
            if not shape or shape.nodeType() != "mesh":
                continue

            members.append(shape.name())

        hosts.maya.lib.assign_look(members, subset="lookMain")

    # Save workfile.
    project = io.find_one({
        "type": "project"
    })
    session = api.Session
    data = {
        "project": {
            "name": project["name"],
            "code": project["data"].get("code")
        },
        "asset": session["AVALON_ASSET"],
        "task": session["AVALON_TASK"],
        "version": 1,
        "user": getpass.getuser()
    }
    anatomy = Anatomy(project["name"])
    template = anatomy.templates["work"]["file"]

    # Define saving file extension
    current_file = host.current_file()
    if current_file:
        # Match the extension of current file
        _, extension = os.path.splitext(current_file)
    else:
        # Fall back to the first extension supported for this host.
        extension = host.file_extensions()[0]

    data["ext"] = extension

    version = api.last_workfile_with_version(
        host.work_root(session), template, data, [data["ext"]]
    )[1]

    if version is None:
        version = 1
    else:
        version += 1

    data["version"] = version

    path = api.format_template_with_optional_keys(data, template)
    host.save_file(path)
