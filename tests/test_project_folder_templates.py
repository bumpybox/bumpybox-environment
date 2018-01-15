from bumpybox_environment import utils
import lib
import test_project_templates as tpt


def get_project_folder():
    project = tpt.get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "library"),
        entity_type="Folder"
    )


def test_project_folder():
    lib.assert_entity(get_project_folder())


def get_project_folder_assetbuild():
    project = tpt.get_project()
    parent = get_project_folder()
    assetbuildtype = utils.mock_entity(
        ("name", "character"),
        entity_type="Type"
    )
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "characterA"),
        ("type", assetbuildtype),
        entity_type="AssetBuild"
    )


def test_project_folder_assetbuild():
    lib.assert_entity(get_project_folder_assetbuild())


def get_project_folder_assetbuild_task():
    project = tpt.get_project()
    assetbuild = get_project_folder_assetbuild()

    return utils.mock_entity(
        ("project", project),
        ("parent", assetbuild),
        ("name", "lookdev"),
        entity_type="Task"
    )


def test_project_folder_assetbuild_task():
    lib.assert_entity(get_project_folder_assetbuild_task())


def get_project_folder_assetbuild_task_file_components():
    task = get_project_folder_assetbuild_task()
    return lib.get_task_file_components(task)


def test_project_folder_assetbuild_task_file_components():
    for entity in get_project_folder_assetbuild_task_file_components():
        lib.assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_components():
    task = get_project_folder_assetbuild_task()
    return lib.get_task_sequences_components(task)


def test_project_folder_assetbuild_task_sequence_components():
    for entity in get_project_folder_assetbuild_task_sequence_components():
        lib.assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_files():
    containers = get_project_folder_assetbuild_task_sequence_components()
    return lib.get_sequence_files(containers)


def test_project_folder_assetbuild_task_sequence_files():
    entities = get_project_folder_assetbuild_task_sequence_files()
    for entity in entities:
        lib.assert_entity(entity)
