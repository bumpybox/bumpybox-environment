import os

import pyblish.api as api

from dirsync import sync


class BumpyboxEnvironmentDeadlineExtractArnoldShaders(api.InstancePlugin):
    """ Add required Arnold shaders. """

    order = api.ExtractorOrder
    label = "Arnold Shaders"
    families = ["deadline", "arnold"]
    match = api.Subset
    hosts = ["maya"]

    def process(self, instance):

        data = instance.data.get("deadlineData", {"job": {}, "plugin": {}})

        target = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline",
            "ARNOLD_PLUGIN_PATH"
        )
        source = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "ARNOLD_PLUGIN_PATH"
            )
        )
        sync(source, target, "sync", create=True, purge=True, modtime=True)

        # Add required environment.
        key_values = {
            "ARNOLD_PLUGIN_PATH": target
        }

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
