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

    # Project/Episode
    mount = "{project.root}"
    templates.extend([
        utils.Template("Project/Episode", mount + "/publish/episodes/{name}"),
        utils.Template("Project/Episode", mount + "/work/episodes/{name}"),
    ])

    # Project/Episode/Task
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Episode/Task",
            mount + "/publish/episodes/{parent.name}/{name}"
        ),
        utils.Template(
            "Project/Episode/Task",
            mount + "/work/episodes/{parent.name}/{name}"
        ),
    ])

    # Project/Episode/Task work files
    mount = "{parent.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Episode"
            "/Task"
            "/.hrox",
            mount + "/work"
            "/episodes"
            "/{parent.name}"
            "/{name}"
            "/{parent.name}_{name}_v{version}{file_type}"
        )
    ])

    # Project/Episode/Asset/AssetVersion/Components
    mount = "{version.task.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Episode"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.hrox",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"
        ),
    ])

    # Project/Episode/Shot
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Episode/Shot",
            mount + "/publish/episodes/{parent.name}/{name}"
        ),
        utils.Template(
            "Project/Episode/Shot",
            mount + "/work/episodes/{parent.name}/{name}"
        ),
    ])

    # Project/Episode/Shot/Task
    mount = "{project.root}"
    templates.extend([
        utils.Template(
            "Project/Episode/Shot/Task",
            mount + "/publish"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
        ),
        utils.Template(
            "Project/Episode/Shot/Task",
            mount + "/work"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Episode/Shot/Task work files
    mount = "{parent.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Task"
            "/.mb",
            mount + "/work"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
            "/{parent.parent.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Task"
            "/.nk",
            mount + "/work"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
            "/{parent.parent.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Task"
            "/.hrox",
            mount + "/work"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
            "/{parent.parent.name}_{parent.name}_{name}_v{version}{file_type}"
        ),
    ])

    # Project/Episode/Shot/Asset/AssetVersion/Components
    mount = "{version.task.project.root}"
    templates.extend([
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.hrox",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/cache"
            "/AssetVersion"
            "/FileComponent"
            "/.abc",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/mov"
            "/AssetVersion"
            "/FileComponent"
            "/.mov",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/audio"
            "/AssetVersion"
            "/FileComponent"
            "/.wav",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/nuke_gizmo"
            "/AssetVersion"
            "/FileComponent"
            "/.gizmo",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr",
            mount + "/publish"
            "/episodes"
            "/{version.asset.parent.parent.name}"
            "/{version.asset.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}"
            "/{version.asset.parent.parent.name}_"
            "{version.asset.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}.%{padding}d{file_type}"
        ),
        utils.Template(
            "Project"
            "/Episode"
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
            "/episodes"
            "/{container.version.asset.parent.parent.name}"
            "/{container.version.asset.parent.name}"
            "/{container.version.task.name}"
            "/v{container.version.version}"
            "/output"
            "/{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}"
            "/{container.version.asset.parent.parent.name}_"
            "{container.version.asset.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
    ])

    return templates
