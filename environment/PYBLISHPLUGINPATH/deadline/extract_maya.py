import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtractMaya(api.InstancePlugin):
    """ Add groups to Maya Submissions. """

    order = api.ExtractorOrder
    label = "Maya"
    families = ["deadline"]
    hosts = ["maya"]

    def process(self, instance):

        data = instance.data.get(
            "deadlineData", {"job": {}, "plugin": {}}
        )

        data["job"]["Group"] = "mtoa"

        instance.data["deadlineData"] = data
