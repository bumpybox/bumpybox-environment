import os

import pyblish.api as api


class BumpyboxEnvironmentDeadlineExtract(api.InstancePlugin):
    """ Add Bumpybox specific submission parameters. """

    order = api.ExtractorOrder
    label = "Deadline"
    families = ["deadline"]

    def process(self, instance):

        data = instance.data.get(
            "deadlineData", {"job": {}, "plugin": {}}
        )

        data["job"]["UserName"] = os.environ["LOGNAME"]

        instance.data["deadlineData"] = data
