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

    templates = []

    # Project/Folder
    mount = "{project.root}"
    templates.extend([
        utils.Template("Project/Folder", mount + "/publish/{name}"),
        utils.Template("Project/Folder", mount + "/work/{name}"),
    ])

    # Project/Folder/AssetBuild
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Folder/AssetBuild",
            mount + "/publish/{parent.name}/{type.name}/{name}"
        ),
        utils.Template(
            "Project/Folder/AssetBuild",
            mount + "/work/{parent.name}/{type.name}/{name}"
        ),
    ])

    # Project/Folder/AssetBuild/Task
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Folder/AssetBuild/Task",
            mount + "/publish"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
        ),
        utils.Template(
            "Project/Folder/AssetBuild/Task",
            mount + "/work"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Folder/AssetBuild/Task work files
    mount = "{parent.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Task"
            "/.mb",
            mount + "/work"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Task"
            "/.nk",
            mount + "/work"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        ),
    ])

    # Project/Folder/AssetBuild/Asset/AssetVersion/Components
    mount = "{version.task.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/cache"
            "/AssetVersion"
            "/FileComponent"
            "/.abc",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/mov"
            "/AssetVersion"
            "/FileComponent"
            "/.mov",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/audio"
            "/AssetVersion"
            "/FileComponent"
            "/.wav",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/nuke_gizmo"
            "/AssetVersion"
            "/FileComponent"
            "/.gizmo",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr",
            mount + "/publish"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.type.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}.%{padding}d{file_type}"
        ),
        utils.Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr"
            "/FileComponent"
            "/.exr",
            "{container.version.task.project.root}"
            "/publish"
            "/{container.version.asset.parent.parent.name}"
            "/{container.version.asset.parent.type.name}"
            "/{container.version.asset.parent.name}"
            "/{container.version.task.name}"
            "/v{container.version.version}"
            "/output"
            "/{container.version.asset.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}"
            "/{container.version.asset.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
    ])

    return templates
