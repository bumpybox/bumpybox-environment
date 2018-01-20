from bumpybox_environment import utils
import lib
import test_project_templates as tpt


def get_project_episode():
    project = tpt.get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "ep0010"),
        entity_type="Episode"
    )


def test_project_episode():
    lib.assert_entity(get_project_episode())


def get_project_episode_task():
    project = tpt.get_project()
    parent = get_project_episode()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_episode_task():
    lib.assert_entity(get_project_episode_task())


def get_project_episode_task_files():
    entities = []

    task = get_project_episode_task()

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

    return entities


def test_project_episode_task_files():
    for entity in get_project_episode_task_files():
        lib.assert_entity(entity)


def get_project_episode_shot():
    project = tpt.get_project()
    parent = get_project_episode()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_episode_shot():
    lib.assert_entity(get_project_episode_shot())


def get_project_episode_shot_task():
    project = tpt.get_project()
    parent = get_project_episode_shot()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "lighting"),
        entity_type="Task"
    )


def test_project_episode_shot_task():
    lib.assert_entity(get_project_episode_shot_task())


def get_project_episode_shot_task_file_components():
    task = get_project_episode_shot_task()
    return lib.get_task_file_components(task)


def test_project_episode_shot_task_file_components():
    for entity in get_project_episode_shot_task_file_components():
        lib.assert_entity(entity)


def get_project_episode_shot_task_sequence_components():
    task = get_project_episode_shot_task()
    return lib.get_task_sequences_components(task)


def test_project_episode_shot_task_sequence_components():
    for entity in get_project_episode_shot_task_sequence_components():
        lib.assert_entity(entity)


def get_project_episode_shot_task_sequence_files():
    containers = get_project_episode_shot_task_sequence_components()
    return lib.get_sequence_files(containers)


def test_project_episode_shot_task_sequence_files():
    entities = get_project_episode_shot_task_sequence_files()
    for entity in entities:
        lib.assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project_episode())
    entities.append(get_project_episode_task())
    entities.extend(get_project_episode_task_files())
    entities.append(get_project_episode_shot())
    entities.append(get_project_episode_shot_task())
    entities.extend(get_project_episode_shot_task_file_components())
    entities.extend(get_project_episode_shot_task_sequence_components())
    entities.extend(get_project_episode_shot_task_sequence_files())

    return entities
