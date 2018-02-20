import pyblish.api


class ExtractDeadlineMaya(pyblish.api.InstancePlugin):
    """Extracts studio data for Deadline."""

    order = pyblish.api.ExtractorOrder - 0.1
    label = "Bumpybox Deadline"
    optional = True
    hosts = ["maya"]
    families = ["deadline"]
    targets = ["process.deadline"]

    def process(self, instance):
        import os
        import time
        import shutil

        import ftrack_api

        data = instance.data.get(
            "deadlineData", {"job": {}, "plugin": {}}
        )

        # Copy scene file to render directory
        basename, ext = os.path.splitext(
            os.path.basename(instance.context.data["currentFile"])
        )
        session = ftrack_api.Session()
        task = session.get("Task", os.environ["FTRACK_TASKID"])
        path = os.path.join(
            task["project"]["root"],
            "render",
            "{0}_{1}{2}".format(basename, time.strftime("%Y%m%d%H%M%S"), ext)
        )
        shutil.copy(instance.context.data["currentFile"], path)

        data["plugin"]["SceneFile"] = path

        # Add script dependency
        destination = os.path.join(
            task["project"]["root"],
            "render",
            "check_scene_file.py"
        )
        if not os.path.exists(destination):
            source = os.path.abspath(
                os.path.join(__file__, "..", "check_scene_file.py")
            )
            shutil.copy(source, destination)

        data["job"]["ScriptDependency0"] = destination

        # Output prefix
        data["plugin"]["OutputFilePrefix"] = "<RenderLayer>/" + basename

        # Set environment
        environment = data["job"].get("EnvironmentKeyValue", {})
        environment["solidangle_LICENSE"] = os.environ["solidangle_LICENSE"]

        data["job"]["EnvironmentKeyValue"] = environment
        instance.data["deadlineData"] = data
