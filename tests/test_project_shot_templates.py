import lib
from bumpybox_environment import utils
import test_project_templates as tpt


def get_project_shot():
    project = tpt.get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_shot():
    lib.assert_entity(get_project_shot())


def get_project_shot_task():
    project = tpt.get_project()
    parent = get_project_shot()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "lighting"),
        entity_type="Task"
    )


def test_project_shot_task():
    lib.assert_entity(get_project_shot_task())


def get_project_shot_task_file_components():
    task = get_project_shot_task()
    return lib.get_task_file_components(task)


def test_project_shot_task_file_components():
    for entity in get_project_shot_task_file_components():
        lib.assert_entity(entity)


def get_project_shot_task_sequence_components():
    task = get_project_shot_task()
    return lib.get_task_sequences_components(task)


def test_project_shot_task_sequence_components():
    for entity in get_project_shot_task_sequence_components():
        lib.assert_entity(entity)


def get_project_shot_task_sequence_files():
    containers = get_project_shot_task_sequence_components()
    return lib.get_sequence_files(containers)


def test_project_shot_task_sequence_files():
    entities = get_project_shot_task_sequence_files()
    for entity in entities:
        lib.assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project_shot())
    entities.append(get_project_shot_task())
    entities.extend(get_project_shot_task_file_components())
    entities.extend(get_project_shot_task_sequence_components())
    entities.extend(get_project_shot_task_sequence_files())

    return entities
