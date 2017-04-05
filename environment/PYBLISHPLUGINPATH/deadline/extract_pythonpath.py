import os

import pyblish.api as api

from dirsync import sync


class BumpyboxEnvironmentDeadlineExtractPYTHONPATH(api.InstancePlugin):
    """ Add event script for updating Ftrack status. """

    order = api.ExtractorOrder
    label = "PYTHONPATH"
    families = ["deadline", "ftrack"]
    match = api.Subset

    def process(self, instance):

        directory = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline",
            "PYTHONPATH"
        )

        sync(
            os.path.join(os.path.dirname(__file__), "PYTHONPATH"),
            directory,
            "sync",
            create=True,
            purge=True,
            modtime=True
        )

        # Add event script to Deadline submission
        data = instance.data.get("deadlineData", {"job": {}, "plugin": {}})

        # Add required environment.
        key_values = {"PYTHONPATH": directory}

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
