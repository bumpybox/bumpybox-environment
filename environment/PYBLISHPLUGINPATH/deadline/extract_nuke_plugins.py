import os

import pyblish.api as api

from dirsync import sync


class BumpyboxEnvironmentDeadlineExtractNukePlugins(api.InstancePlugin):
    """ Add nuke plugins. """

    order = api.ExtractorOrder
    label = "Nuke Plugins"
    families = ["deadline"]
    hosts = ["nuke"]

    def process(self, instance):

        data = instance.data.get("deadlineData", {"job": {}, "plugin": {}})

        target = os.path.join(
            os.path.dirname(instance.context.data["currentFile"]),
            "workspace",
            "deadline",
            "NUKE_PATH"
        )
        source = os.path.abspath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "NUKE_PATH"
            )
        )
        sync(source, target, "sync", create=True, purge=True, modtime=True)

        # Add required environment.
        key_values = {
            "NUKE_PATH": target
        }

        if "EnvironmentKeyValue" in data["job"]:
            data["job"]["EnvironmentKeyValue"].update(key_values)
        else:
            data["job"]["EnvironmentKeyValue"] = key_values

        # Setting data
        instance.data["deadlineData"] = data
