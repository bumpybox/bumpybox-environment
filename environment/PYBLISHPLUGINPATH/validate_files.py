from pyblish import api


class RepairFiles(api.Action):

    label = "Repair"
    icon = "wrench"
    on = "failed"

    def process(self, context, plugin):
        import shutil
        import os

        # Get the errored instances
        failed = []
        for result in context.data["results"]:
            if (result["error"] is not None and result["instance"] is not None
               and result["instance"] not in failed):
                failed.append(result["instance"])

        # Apply pyblish.logic to get the instances for the plug-in
        instances = api.instances_by_plugin(failed, plugin)

        plugin = ValidateFiles()
        for instance in instances:
            src = instance[0].fileTextureName.get()
            dst = plugin.get_path(instance)

            if not os.path.exists(os.path.dirname(dst)):
                os.makedirs(os.path.dirname(dst))

            shutil.copy(src, dst)

            instance[0].fileTextureName.set(dst)


class ValidateFiles(api.InstancePlugin):
    """Validate files used in scene are published."""

    order = api.ValidatorOrder
    families = ["file"]
    label = "Files"
    targets = ["process"]
    actions = [RepairFiles]
    optional = True

    def process(self, instance):
        import os

        current_path = instance[0].fileTextureName.get()
        expected_path = self.get_path(instance)

        # Its acceptable to have textures in the same folder as the
        # expected_path.
        if os.path.dirname(current_path) == os.path.dirname(expected_path):
            return

        msg = "Expected \"{0}\" to be at \"{1}\"".format(
            current_path, expected_path
        )
        assert current_path == expected_path, msg

    def get_path(self, instance):
        import os

        scene_name = os.path.splitext(
            os.path.basename(instance.context.data["currentFile"])
        )[0]
        ext = os.path.splitext(instance[0].fileTextureName.get())[1]
        items = os.path.abspath(
            os.path.join(
                instance.context.data["currentFile"],
                "..",
                "{0}_{1}{2}".format(
                    scene_name, instance.data["name"], ext
                )
            )
        ).split(os.sep)
        for n, i in enumerate(items):
            if i == "work":
                items[n] = "maps"
                break

        return "/".join(items)
