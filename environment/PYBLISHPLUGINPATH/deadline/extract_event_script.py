import os
import shutil

import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtractEventScript(api.InstancePlugin):
    """ Add event script for updating Ftrack status. """

    order = api.ExtractorOrder
    label = "Event Script"
    families = ["deadline", "ftrack"]
    match = api.Subset

    def process(self, instance):

        data = instance.data.get("deadlineData", {"job": {}, "plugin": {}})

        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline"
        )

        if not os.path.exists(directory):
            os.makedirs(directory)

        shutil.copy(
            os.path.join(
                os.path.dirname(__file__),
                "event_script.py"
            ),
            os.path.join(directory, "event_script.py")
        )

        # Add event script to Deadline submission
        path = os.path.join(directory, "event_script.py")
        if "ExtraInfoKeyValue" in data["job"]:
            data["job"]["ExtraInfoKeyValue"]["EventScript"] = path
        else:
            data["job"]["ExtraInfoKeyValue"] = {"EventScript": path}

        # Add required environment.
        key_values = {
            "FTRACK_SERVER": os.environ["FTRACK_SERVER"],
            "FTRACK_APIKEY": os.environ["FTRACK_APIKEY"],
            "LOGNAME": os.environ["LOGNAME"],
            "FTRACK_TASKID": os.environ["FTRACK_TASKID"],
        }

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
