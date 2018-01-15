import platform

from bumpybox_environment import utils


def register():
    """Register templates.

    Templates are named according to the entity in the hierarchy,
    they aim to solve paths for.
    For example a template named "Project" is only for paths for the project.
    Nested entity types are specified with a path separator, for example
    "Project/Shot" deals with paths for shots under the project.
    To specify dealing with certain file types, the file types extension is
    added. For example a template named "Project/.nk" deals with Nuke script
    paths under the project.
    It is assumed that asset versions are children of the asset, resulting in a
    path "Project/Asset/AssetVersion".
    """

    system_name = platform.system().lower()
    if system_name != "windows":
        system_name = "unix"

    templates = []

    # Project
    mount = "{disk." + system_name + "}/{root}"
    templates.extend([
        utils.Template("Project", mount),
        utils.Template("Project", mount + "/in"),
        utils.Template("Project", mount + "/out"),
        utils.Template("Project", mount + "/publish"),
        utils.Template("Project", mount + "/work"),
    ])

    # Project/Task
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        utils.Template("Project/Task", mount + "/work/tasks/{name}"),
    ])

    # Project/Task work files
    mount = (
        "{parent.disk." + system_name + "}/{parent.root}"
    )
    templates.extend([
        utils.Template(
            "Project"
            "/Task"
            "/.hrox",
            mount + "/work"
            "/tasks"
            "/{name}"
            "/{name}_v{version}{file_type}"
        ),
    ])

    # Project/Asset/AssetVersion/Components
    mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}"
    )
    templates.extend([
        utils.Template(
            "Project"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.hrox",
            mount + "/publish"
            "/tasks"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.name}_v{version.version}{file_type}"
        )
    ])

    return templates
