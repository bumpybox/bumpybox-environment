import pyblish.api


class ExtractDeadline(pyblish.api.InstancePlugin):
    """Extracts studio data for Deadline."""

    order = pyblish.api.ExtractorOrder
    label = "Bumpybox Deadline"
    optional = True
    hosts = ["maya"]
    families = ["deadline"]
    targets = ["process.deadline"]

    def process(self, instance):
        import os

        data = instance.data.get(
            "deadlineData", {"job": {}, "plugin": {}}
        )

        environment = data["job"].get("EnvironmentKeyValue", {})

        environment["solidangle_LICENSE"] = os.environ["solidangle_LICENSE"]

        data["job"]["EnvironmentKeyValue"] = environment
        instance.data["deadlineData"] = data
