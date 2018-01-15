import os

import lucidity


class mock_entity(dict):
    """Mock entity for faking Ftrack entities
    Requires keyword argument "entity_type" on creation.
    """

    def __init__(self, *args, **kwargs):
        dict.__init__(self, args)

        if "entity_type" not in kwargs.keys():
            raise ValueError('Need the keyword argument "entity_type"')

        self.__dict__ = kwargs


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
