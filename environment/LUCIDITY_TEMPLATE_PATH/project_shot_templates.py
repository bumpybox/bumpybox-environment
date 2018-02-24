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

    # Project/Shot
    mount = "{project.root}"
    templates.extend([
        utils.Template("Project/Shot", mount + "/publish/shots/{name}"),
        utils.Template("Project/Shot", mount + "/work/shots/{name}"),
    ])

    # Project/Shot/Task
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Shot/Task",
            mount + "/publish"
            "/shots"
            "/{parent.name}"
            "/{name}"
        ),
        utils.Template(
            "Project/Shot/Task",
            mount + "/work"
            "/shots"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Shot/Task work files
    mount = "{parent.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Shot"
            "/Task"
            "/.mb",
            mount + "/work"
            "/shots"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Shot"
            "/Task"
            "/.nk",
            mount + "/work"
            "/shots"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Shot"
            "/Task"
            "/.hrox",
            mount + "/work"
            "/shots"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        ),
    ])

    # Project/Shot/Asset/AssetVersion/Components
    mount = "{version.task.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/shots"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/shots"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.hrox",
            mount + "/publish"
            "/shots"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/cache"
            "/AssetVersion"
            "/FileComponent"
            "/.abc",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/mov"
            "/AssetVersion"
            "/FileComponent"
            "/.mov",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/audio"
            "/AssetVersion"
            "/FileComponent"
            "/.wav",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/nuke_gizmo"
            "/AssetVersion"
            "/FileComponent"
            "/.gizmo",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/FileComponent"
            "/.exr",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/FileComponent"
            "/.jpg",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/FileComponent"
            "/.jpeg",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/FileComponent"
            "/.png",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr"
            "/FileComponent"
            "/.exr",
            "{container.version.task.project.root}"
            "/publish"
            "/shots"
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
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.jpg",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.jpg"
            "/FileComponent"
            "/.jpg",
            "{container.version.task.project.root}"
            "/publish"
            "/shots"
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
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.jpeg",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.jpeg"
            "/FileComponent"
            "/.jpeg",
            "{container.version.task.project.root}"
            "/publish"
            "/shots"
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
        utils.Template(
            "Project"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.png",
            mount + "/publish"
            "/shots"
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
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.png"
            "/FileComponent"
            "/.png",
            "{container.version.task.project.root}"
            "/publish"
            "/shots"
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
