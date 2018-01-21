import pyblish.api


class BumpyboxExtractFtrackComponents(pyblish.api.InstancePlugin):
    """Extracts the data for Ftrack components."""

    order = pyblish.api.ExtractorOrder
    label = "Bumpybox Components"
    optional = True
    families = ["ftrack"]

    def process(self, instance):

        instance.data["asset_data"] = {
            "name": "{0}_{1}".format(
                instance.context.data["ftrackTask"]["name"],
                instance.data["name"]
            )
        }
        instance.data["assetversion_data"] = {
            "metadata": {"instance_name": instance.data["name"]}
        }
        instance.data["component_data"] = {"name": "main"}
        instance.data["component_overwrite"] = True
