import os
import platform

import lucidity


class Template(lucidity.Template):

    def get_parents(self, entity, parents):
        """Recursive iterate to find all parents.

        For AssetVersion where no parent is present, the asset is assumed as
        parent.
        For SequenceComponent and FileComponent where no parent is present, the
        asset version is assumed as parent.
        """

        try:
            parent = entity["parent"]
            if parent:
                parents.append(parent)
                return self.get_parents(parent, parents)
        except KeyError:
            if entity.entity_type == "AssetVersion":
                parents.append(entity["asset"])
                return self.get_parents(entity["asset"], parents)

            if entity.entity_type == "FileComponent":

                parent = entity["version"]
                # Assuming its in a container, if there are no version.
                if parent:
                    parents.append(entity["version"])
                else:
                    parent = entity["container"]
                    parents.append(entity["container"])
                return self.get_parents(parent, parents)

            if entity.entity_type == "SequenceComponent":
                parents.append(entity["version"])
                return self.get_parents(entity["version"], parents)

        return parents

    def get_entity_type_path(self, entities):
        """Get the entity type path from a list of entities

        The returned path is a list of entity types separated by a path
        separator:
            "[entity_type]/[entity_type]/[entity_type]"
            "Project/Asset/AssetVersion"

        The "short" data member (asset type code) is used for components. This
        results in paths like this:
            Project/Asset/[short]
            Project/Asset/upload

        The "file_type" data member (extension) is used for components. This
        results in paths like this:
            "Project/Asset/[short]/AssetVersion/FileComponent/[file_type]"
            "Project/Asset/upload/AssetVersion/FileComponent/.txt"
        """

        path_items = []
        for entity in entities:
            path_items.append(entity.entity_type)

            try:
                if entity["type"]:
                    path_items.append(entity["type"]["short"])
            except KeyError:
                pass

            try:
                path_items.append(entity["file_type"])
            except KeyError:
                pass

        return "/".join(path_items)

    def get_template_name(self, entity):
        """Convenience method for getting the template name

        The template name is generated from the entity's parents, and their
        entity type.
        """

        entities = list(reversed(self.get_parents(entity, [])))
        entities.append(entity)
        return self.get_entity_type_path(entities)

    def get_valid_templates(self, entity, templates):

        results = []
        template_name = self.get_template_name(entity)
        try:
            template_name = entity["metadata"]["lucidity_template_name"]
        except KeyError:
            pass

        for template in templates:
            if template.name == template_name:
                results.append(template)

        return results

    def format(self, data):

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "AssetVersion":
            version_string = str(data["version"]).zfill(4)
            data["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "FileComponent":
            if data["version"]:
                version_string = str(data["version"]["version"]).zfill(4)
                data["version"]["version"] = version_string
            else:
                version_string = str(
                    data["container"]["version"]["version"]
                ).zfill(4)
                data["container"]["version"]["version"] = version_string

        # "version" data member needs to be convert from integer to string.
        if data.entity_type == "SequenceComponent":
            version_string = str(data["version"]["version"]).zfill(4)
            data["version"]["version"] = version_string

            # "padding" data member needs to be convert from integer to string.
            padding_string = str(data["padding"]).zfill(2)
            data["padding"] = padding_string

        if data.entity_type == "Task" and "version" in data.keys():
            version_string = str(data["version"]).zfill(4)
            data["version"] = version_string

        return os.path.abspath(
            super(Template, self).format(data)
        ).replace("\\", "/")


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
        Template("Project", mount),
        Template("Project", mount + "/in"),
        Template("Project", mount + "/out"),
        Template("Project", mount + "/publish"),
        Template("Project", mount + "/work"),
    ])

    # Project/Folder
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template("Project/Folder", mount + "/publish/{name}"),
        Template("Project/Folder", mount + "/work/{name}"),
    ])

    # Project/Folder/AssetBuild
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template(
            "Project/Folder/AssetBuild",
            mount + "/publish/{parent.name}/{type.name}/{name}"
        ),
        Template(
            "Project/Folder/AssetBuild",
            mount + "/work/{parent.name}/{type.name}/{name}"
        ),
    ])

    # Project/Folder/AssetBuild/Task
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template(
            "Project/Folder/AssetBuild/Task",
            mount + "/publish"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
        ),
        Template(
            "Project/Folder/AssetBuild/Task",
            mount + "/work"
            "/{parent.parent.name}"
            "/{parent.type.name}"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Folder/AssetBuild/Task work files
    mount = (
        "{parent.project.disk." + system_name + "}/"
        "{parent.project.root}"
    )
    templates.extend([
        Template(
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
        Template(
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
    mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}"
    )
    templates.extend([
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/cache"
            "/AssetVersion"
            "/FileComponent"
            "/.abc",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/mov"
            "/AssetVersion"
            "/FileComponent"
            "/.mov",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/nuke_gizmo"
            "/AssetVersion"
            "/FileComponent"
            "/.gizmo",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Folder"
            "/AssetBuild"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr",
            mount + "/publish"
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.type.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}.%{padding}d{file_type}"
        ),
        Template(
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
            "{container.version.task.project.disk." + system_name + "}"
            "/{container.version.task.project.root}"
            "/publish"
            "/{container.version.task.parent.parent.name}"
            "/{container.version.task.parent.type.name}"
            "/{container.version.task.parent.name}"
            "/{container.version.task.name}"
            "/v{container.version.version}"
            "/output"
            "/{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}"
            "/{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
    ])

    # Project/Shot
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template("Project/Shot", mount + "/publish/shots/{name}"),
        Template("Project/Shot", mount + "/work/shots/{name}"),
    ])

    # Project/Shot/Task
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template(
            "Project/Shot/Task",
            mount + "/publish"
            "/shots"
            "/{parent.name}"
            "/{name}"
        ),
        Template(
            "Project/Shot/Task",
            mount + "/work"
            "/shots"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Shot/Task work files
    mount = (
        "{parent.project.disk." + system_name + "}/"
        "{parent.project.root}"
    )
    templates.extend([
        Template(
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
        Template(
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
    ])

    # Project/Shot/Asset/AssetVersion/Components
    mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}"
    )
    templates.extend([
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/source"
            "/AssetVersion"
            "/FileComponent"
            "/.nk",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.name}_{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/scene"
            "/AssetVersion"
            "/FileComponent"
            "/.mb",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/cache"
            "/AssetVersion"
            "/FileComponent"
            "/.abc",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/mov"
            "/AssetVersion"
            "/FileComponent"
            "/.mov",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/nuke_gizmo"
            "/AssetVersion"
            "/FileComponent"
            "/.gizmo",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr",
            mount + "/publish"
            "/shots"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}"
            "/{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}.%{padding}d{file_type}"
        ),
        Template(
            "Project"
            "/Shot"
            "/Asset"
            "/img"
            "/AssetVersion"
            "/SequenceComponent"
            "/.exr"
            "/FileComponent"
            "/.exr",
            "{container.version.task.project.disk." + system_name + "}"
            "/{container.version.task.project.root}"
            "/publish"
            "/shots"
            "/{container.version.task.parent.name}"
            "/{container.version.task.name}"
            "/v{container.version.version}"
            "/output"
            "/{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}"
            "/{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
    ])

    # Project/Episode
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template("Project/Episode", mount + "/publish/episodes/{name}"),
        Template("Project/Episode", mount + "/work/episodes/{name}"),
    ])

    # Project/Episode/Shot
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template(
            "Project/Episode/Shot",
            mount + "/publish/episodes/{parent.name}/{name}"
        ),
        Template(
            "Project/Episode/Shot",
            mount + "/work/episodes/{parent.name}/{name}"
        ),
    ])

    # Project/Episode/Shot/Task
    mount = "{project.disk." + system_name + "}/{project.root}"
    templates.extend([
        Template(
            "Project/Episode/Shot/Task",
            mount + "/publish"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
        ),
        Template(
            "Project/Episode/Shot/Task",
            mount + "/work"
            "/episodes"
            "/{parent.parent.name}"
            "/{parent.name}"
            "/{name}"
        ),
    ])

    # Project/Episode/Shot/Task work files
    mount = (
        "{parent.project.disk." + system_name + "}/"
        "{parent.project.root}"
    )
    templates.extend([
        Template(
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
        Template(
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
    ])

    # Project/Episode/Shot/Asset/AssetVersion/Components
    mount = (
        "{version.task.project.disk." + system_name + "}/"
        "{version.task.project.root}"
    )
    templates.extend([
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"
        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "v{version.version}{file_type}"

        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}{file_type}"
        ),
        Template(
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
            "/{version.task.parent.parent.name}"
            "/{version.task.parent.name}"
            "/{version.task.name}"
            "/v{version.version}"
            "/output"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}"
            "/{version.task.parent.parent.name}_"
            "{version.task.parent.name}_"
            "{version.task.name}_"
            "{version.metadata.instance_name}_"
            "v{version.version}.%{padding}d{file_type}"
        ),
        Template(
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
            "{container.version.task.project.disk." + system_name + "}"
            "/{container.version.task.project.root}"
            "/publish"
            "/episodes"
            "/{container.version.task.parent.parent.name}"
            "/{container.version.task.parent.name}"
            "/{container.version.task.name}"
            "/v{container.version.version}"
            "/output"
            "/{container.version.task.parent.parent.name}_"
            "{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}"
            "/{container.version.task.parent.parent.name}_"
            "{container.version.task.parent.name}_"
            "{container.version.task.name}_"
            "{container.version.metadata.instance_name}_"
            "v{container.version.version}.{name}{file_type}"
        ),
    ])

    return templates
