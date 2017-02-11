import pyblish.api as api
import ftrack_locations


class BumpyboxEnvironmentFtrackExtractSceneComponent(api.InstancePlugin):
    """ Appending output files from local extraction as components. """

    order = api.ExtractorOrder
    label = "Scene Component"
    families = ["scene"]

    def process(self, instance):

        if "collection" not in instance.data:

            # Add ftrack family
            families = instance.data.get("families", [])
            instance.data["families"] = families + ["ftrack"]

            # Get location
            session = instance.context.data["ftrackSession"]
            location = ftrack_locations.get_new_location(session)

            # Add component
            components = instance.data.get("ftrackComponentsList", [])
            components.append({
                "assettype_data": {"short": "scene"},
                "assetversion_data": {
                    "version": instance.context.data["version"]
                },
                "component_data": {
                    "name": api.current_host(),
                },
                "component_path": instance.context.data["currentFile"],
                "component_overwrite": True,
                "component_location": location,
            })
            instance.data["ftrackComponentsList"] = components
