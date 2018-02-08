import lucidity

from bumpybox_environment import utils


def assert_entity(entity):
    templates = lucidity.discover_templates()
    msg = (
        "No valid templates found for template name: \"{0}\", and entity: "
        "\"{1}\"".format(templates[0].get_template_name(entity), entity)
    )
    assert templates[0].get_valid_templates(entity, templates), msg

    get_resolved_paths(entity)


def get_resolved_paths(entity):
    templates = lucidity.discover_templates()
    valid_templates = templates[0].get_valid_templates(entity, templates)
    resolved_paths = []
    for template in valid_templates:
        try:
            resolved_paths.append(template.format(entity))
        except lucidity.error.FormatError as e:
            msg = e.message + "\nTemplate name: {0}".format(template.name)
            raise type(e)(msg)

    return resolved_paths


def get_task_file_components(task):

    entities = []

    # Maya work file
    entities.append(
        utils.mock_entity(
            ("parent", task["parent"]),
            ("version", 1),
            ("file_type", ".mb"),
            ("name", task["name"]),
            entity_type="Task"
        )
    )

    # Nuke work file
    entities.append(
        utils.mock_entity(
            ("parent", task["parent"]),
            ("version", 1),
            ("file_type", ".nk"),
            ("name", task["name"]),
            entity_type="Task"
        )
    )

    # NukeStudio work file
    entities.append(
        utils.mock_entity(
            ("parent", task["parent"]),
            ("version", 1),
            ("file_type", ".hrox"),
            ("name", task["name"]),
            entity_type="Task"
        )
    )

    # Maya source
    assettype = utils.mock_entity(
        ("short", "source"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".mb"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Nuke source
    assettype = utils.mock_entity(
        ("short", "source"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".nk"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # NukeStudio source
    assettype = utils.mock_entity(
        ("short", "source"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".hrox"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Maya binary
    assettype = utils.mock_entity(
        ("short", "scene"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".mb"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Alembic
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".abc"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Alembic
    assettype = utils.mock_entity(
        ("short", "cache"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".abc"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Movie
    assettype = utils.mock_entity(
        ("short", "mov"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".mov"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Movie
    assettype = utils.mock_entity(
        ("short", "audio"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".wav"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    # Gizmo
    assettype = utils.mock_entity(
        ("short", "nuke_gizmo"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("file_type", ".gizmo"),
            ("name", "main"),
            entity_type="FileComponent"
        )
    )

    return entities


def get_task_sequences_components(task):
    entities = []

    # EXR
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ".exr"),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
    )

    # JPG
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ".jpg"),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
    )

    # JPG
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ".jpeg"),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
    )

    # JPG
    assettype = utils.mock_entity(
        ("short", "img"),
        entity_type="Type"
    )
    asset = utils.mock_entity(
        ("parent", task["parent"]),
        ("type", assettype),
        entity_type="Asset"
    )
    assetversion = utils.mock_entity(
        ("asset", asset),
        ("task", task),
        ("version", 1),
        ("metadata", {"instance_name": "instanceName"}),
        entity_type="AssetVersion"
    )
    entities.append(
        utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ".png"),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
    )

    return entities


def get_sequence_files(containers):
    entities = []
    for container in containers:
        entity = utils.mock_entity(
            ("version", None),
            ("container", container),
            ("file_type", container["file_type"]),
            ("name", "1001"),
            entity_type="FileComponent"
        )
        entities.append(entity)
    return entities
