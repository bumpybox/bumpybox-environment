import os
import shutil

import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtractEventScript(api.InstancePlugin):
    """ Add event script for updating Ftrack status. """

    order = api.ExtractorOrder
    label = "Event Script"
    families = ["deadline"]

    def copytree(self, src, dst, symlinks=False, ignore=None):
        for item in os.listdir(src):
            s = os.path.join(src, item)
            d = os.path.join(dst, item)
            if os.path.isdir(s):
                shutil.copytree(s, d, symlinks, ignore)
            else:
                shutil.copy2(s, d)

    def process(self, instance):

        data = instance.data.get("deadlineData", {"job": {}, "plugin": {}})

        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline"
        )

        if not os.path.exists(directory):
            os.makedirs(directory)

        # Copy required modules
        if os.path.exists(os.path.join(directory, "PYTHONPATH")):
            shutil.rmtree(os.path.join(directory, "PYTHONPATH"))
        self.copytree(
            os.path.join(
                os.path.dirname(__file__),
                "deadline_event_script",
                "PYTHONPATH"
            ),
            os.path.join(directory, "PYTHONPATH")
        )

        shutil.copy(
            os.path.join(
                os.path.dirname(__file__),
                "deadline_event_script",
                "deadline_script.py"
            ),
            os.path.join(directory, "deadline_script.py")
        )

        # Add event script to Deadline submission
        path = os.path.join(directory, "deadline_script.py")
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
            "PYTHONPATH": os.path.join(directory, "PYTHONPATH")
        }

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
