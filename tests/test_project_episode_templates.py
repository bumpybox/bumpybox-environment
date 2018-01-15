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
