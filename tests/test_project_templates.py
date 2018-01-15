from bumpybox_environment import utils
import lib


def get_project():
    return utils.mock_entity(
        ("disk", {"windows": "//disk", "unix": "//disk"}),
        ("root", "test_project"),
        entity_type="Project"
    )


def test_project():
    lib.assert_entity(get_project())


def get_project_task():
    project = get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_task():
    lib.assert_entity(get_project_task())


def get_project_task_file_components():
    task = get_project_task()

    entities = []

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
            ("file_type", ".hrox"),
            entity_type="FileComponent"
        )
    )

    return entities


def test_project_task_file_components():
    for entity in get_project_task_file_components():
        lib.assert_entity(entity)
