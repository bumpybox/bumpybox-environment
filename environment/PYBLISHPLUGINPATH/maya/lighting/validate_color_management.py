import pymel.core as pc

import pyblish.api as api


class BumpyboxEnvironmentMayaValidateColorManagement(api.InstancePlugin):
    """ Validate that color management is turned on. """

    order = api.ValidatorOrder
    label = "Color Management"
    families = ["scene"]
    optional = True
    hosts = ["maya"]

    def process(self, instance):

        msg = "Color Management is not enabled."
        assert pc.colorManagementPrefs(cmEnabled=True, query=True), msg
