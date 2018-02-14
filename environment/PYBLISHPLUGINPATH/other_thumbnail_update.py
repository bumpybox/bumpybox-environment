import pyblish.api


class FtrackUpdateThumbnails(pyblish.api.InstancePlugin):
    """Update thumbnails on task and shot in Ftrack."""

    order = pyblish.api.IntegratorOrder + 1
    label = "Update Task and Shot thumbnail."
    families = ["review"]

    def process(self, instance):

        for data in instance.data.get("ftrackComponentsList", []):
            if data.get("thumbnail", False):
                task = instance.context.data["ftrackTask"]
                task["thumbnail_id"] = data["component"]["id"]
                parent = data["component"]["version"]["asset"]["parent"]
                parent["thumbnail_id"] = data["component"]["id"]

                instance.context.data["ftrackSession"].commit()
