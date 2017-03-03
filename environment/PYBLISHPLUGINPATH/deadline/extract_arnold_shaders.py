import os
import shutil

import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtractArnoldShaders(api.InstancePlugin):
    """ Add required Arnold shaders. """

    order = api.ExtractorOrder
    label = "Arnold Shaders"
    families = ["deadline"]
    hosts = ["maya"]

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
        arnold_path = os.path.join(directory, "ARNOLD_PLUGIN_PATH")
        if not os.path.exists(arnold_path):
            os.makedirs(arnold_path)

        src = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "ARNOLD_PLUGIN_PATH"
            )
        )

        for f in os.listdir(src):
            shutil.copy(os.path.join(src, f), os.path.join(arnold_path, f))

        # Add required environment.
        key_values = {
            "ARNOLD_PLUGIN_PATH": arnold_path
        }

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
