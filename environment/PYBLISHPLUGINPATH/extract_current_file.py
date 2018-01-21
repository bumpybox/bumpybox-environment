import pyblish.api


class ExtractCurrentFile(pyblish.api.InstancePlugin):
    """Extracts the current file to an Ftrack component."""

    order = pyblish.api.ExtractorOrder
    label = "Current File"
    optional = True
    hosts = ["nuke", "nukeassist", "nukestudio", "maya"]
    families = ["source"]

    def process(self, instance):

        instance.data["ftrackComponentsList"] = [
            {
              "assettype_data": {
                "short": "source",
              },
              "assetversion_data": {
                "version": instance.context.data["version"],
              },
              "component_path": instance.context.data["currentFile"],
              "component_overwrite": True
            }
        ]

        instance.data["output_path"] = instance.context.data["currentFile"]
