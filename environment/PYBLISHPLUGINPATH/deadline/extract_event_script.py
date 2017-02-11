import os
import shutil

import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtractEventScript(api.InstancePlugin):
    """ Appending output files from local extraction as components. """

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

        data = instance.data.get(
            "deadlineData", {"job": {}, "plugin": {}}
        )

        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline_event_script"
        )

        # Copy required modules
        shutil.rmtree(directory)
        self.copytree(
            os.path.join(os.path.dirname(__file__), "deadline_event_script"),
            directory
        )

        # Add event script to Deadline submission
        path = os.path.join(directory, "deadline_event_script.py")
        if "ExtraInfoKeyValue" in data["job"]:
            data["job"]["ExtraInfoKeyValue"]["EventScript"] = path
        else:
            data["job"]["ExtraInfoKeyValue"] = {"EventScript": path}

        # Setting data
        instance.data["deadlineData"] = data
