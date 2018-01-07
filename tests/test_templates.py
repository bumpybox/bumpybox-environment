import os

import lucidity

from bumpybox_environment import utils


def get_test_paths():
    return [
        "//disk/test_project/in",
        "//disk/test_project/out",

        "//disk/test_project/publish",

        "//disk/test_project/publish/library",
        "//disk/test_project/publish/library/character/characterA",
        "//disk/test_project/publish/library/character/characterA/lookdev",

        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/characterA_lookdev_v0001.mb",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/output/characterA_lookdev_instanceName_v0001.mb",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/output/characterA_lookdev_instanceName_v0001.abc",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/output/characterA_lookdev_instanceName_v0001.mov",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/output/characterA_lookdev_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/maya/output/characterA_lookdev_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/nuke/characterA_lookdev_v0001.nk",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/nuke/output/characterA_lookdev_instanceName_v0001.gizmo",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/nuke/output/characterA_lookdev_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/nuke/output/characterA_lookdev_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/shots/sq0010",
        "//disk/test_project/publish/shots/sh0010/lighting",

        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/"
        "sh0010_lighting_v0001.mb",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/output/"
        "sh0010_lighting_instanceName_v0001.mb",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/output/"
        "sh0010_lighting_instanceName_v0001.abc",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/output/"
        "sh0010_lighting_instanceName_v0001.mov",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/output/"
        "sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/maya/output/"
        "sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/shots/sh0010/lighting/v0001/nuke/"
        "sh0010_lighting_v0001.nk",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/nuke/output/"
        "sh0010_lighting_instanceName_v0001.gizmo",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/nuke/output/"
        "sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/nuke/output/"
        "sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/sequences/sq0010",
        "//disk/test_project/publish/sequences/sq0010/sh0010",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting",

        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/sq0010_sh0010_lighting_v0001.mb",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/output/sq0010_sh0010_lighting_instanceName_v0001.mb",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/output/sq0010_sh0010_lighting_instanceName_v0001.abc",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/output/sq0010_sh0010_lighting_instanceName_v0001.mov",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/output/sq0010_sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "maya/output/sq0010_sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "nuke/sq0010_sh0010_lighting_v0001.nk",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "nuke/output/sq0010_sh0010_lighting_instanceName_v0001.gizmo",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "nuke/output/sq0010_sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/sequences/sq0010/sh0010/lighting/v0001/"
        "nuke/output/sq0010_sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/episodes/ep0010",
        "//disk/test_project/publish/episodes/ep0010/sq0010",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting",

        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/ep0010_sq0010_sh0010_lighting_v0001.mb",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.mb",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.abc",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.mov",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/maya/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/nuke/ep0010_sq0010_sh0010_lighting_v0001.nk",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/nuke/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.gizmo",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/nuke/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/episodes/ep0010/sq0010/sh0010/lighting/"
        "v0001/nuke/output/"
        "ep0010_sq0010_sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/work",

        "//disk/test_project/work/library",
        "//disk/test_project/work/library/character/characterA",
        "//disk/test_project/work/library/character/characterA/lookdev",

        "//disk/test_project/work/library/character/characterA/lookdev/maya/"
        "characterA_lookdev_v0001.mb",

        "//disk/test_project/work/library/character/characterA/lookdev/nuke/"
        "characterA_lookdev_v0001.nk",

        "//disk/test_project/work/tasks/editing",
        "//disk/test_project/work/tasks/editing/nukestudio/editing_v0001.hrox",

        "//disk/test_project/work/shots/sh0010",
        "//disk/test_project/work/shots/sh0010/lighting",

        "//disk/test_project/work/shots/sh0010/lighting/maya/"
        "sh0010_lighting_v0001.mb",

        "//disk/test_project/work/shots/sh0010/lighting/nuke/"
        "sh0010_lighting_v0001.nk",

        "//disk/test_project/work/sequences/sq0010",
        "//disk/test_project/work/sequences/sq0010/sh0010",
        "//disk/test_project/work/sequences/sq0010/sh0010/lighting",

        "//disk/test_project/work/sequences/sq0010/sh0010/lighting/maya/"
        "sq0010_sh0010_lighting_v0001.mb",

        "//disk/test_project/work/sequences/sq0010/sh0010/lighting/nuke/"
        "sq0010_sh0010_lighting_v0001.nk",

        "//disk/test_project/work/episodes/ep0010",
        "//disk/test_project/work/episodes/ep0010/sq0010",
        "//disk/test_project/work/episodes/ep0010/sq0010/sh0010",
        "//disk/test_project/work/episodes/ep0010/sq0010/sh0010/lighting",

        "//disk/test_project/work/episodes/ep0010/sq0010/sh0010/lighting/maya/"
        "ep0010_sq0010_sh0010_lighting_v0001.mb",

        "//disk/test_project/work/episodes/ep0010/sq0010/sh0010/lighting/nuke/"
        "ep0010_sq0010_sh0010_lighting_v0001.nk",
    ]


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


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in paths:
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in template_paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def test_unused_templates():
    templates = lucidity.discover_templates()

    used_templates = []
    for entity in get_entities():
        valid_templates = templates[0].get_valid_templates(entity, templates)
        used_templates.extend(valid_templates)

    # Cover templates not used
    unused_templates = list(set(templates) - set(used_templates))
    msg = "Templates not used:"
    for template in unused_templates:
        msg += "\n{0}".format(template)
    assert not unused_templates, msg


def test_excess_templates():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def generate_work_file_tasks(parent, project, name, type_name):
    entities = []

    for ext in utils.workfile_extensions:
        task = utils.mock_entity(
            ("parent", parent),
            ("project", project),
            ("version", 1),
            ("file_type", ext),
            ("name", name),
            ("type", {"name": type_name}),
            entity_type="Task"
        )
        entities.append(task)

    return entities


def generate_file_components(task):
    entities = []
    for ext, short in utils.single_files.iteritems():
        assettype = utils.mock_entity(
            ("short", short),
            entity_type="Type"
        )
        asset = utils.mock_entity(
            ("parent", task["parent"]),
            ("type", assettype),
            ("name", "{0}_instanceName".format(task["name"])),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", task),
            ("version", 1),
            entity_type="AssetVersion"
        )
        entity = utils.mock_entity(
            ("version", assetversion),
            ("file_type", ext),
            ("name", "main"),
            entity_type="FileComponent"
        )
        entities.append(entity)

    return entities


def generate_sequence_components(task):
    entities = []

    for ext, short in utils.sequence_files.iteritems():
        assettype = utils.mock_entity(
            ("short", short),
            entity_type="Type"
        )
        asset = utils.mock_entity(
            ("parent", task["parent"]),
            ("type", assettype),
            ("name", "{0}_instanceName".format(task["name"])),
            entity_type="Asset"
        )
        assetversion = utils.mock_entity(
            ("asset", asset),
            ("task", task),
            ("version", 1),
            entity_type="AssetVersion"
        )
        entity = utils.mock_entity(
            ("version", assetversion),
            ("name", "main"),
            ("file_type", ext),
            ("padding", 4),
            entity_type="SequenceComponent"
        )
        entities.append(entity)

    return entities


def generate_container_members(containers):
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


def get_project():
    return utils.mock_entity(
        ("disk", {"windows": "//disk", "unix": "//disk"}),
        ("root", "test_project"),
        entity_type="Project"
    )


def test_project():
    assert_entity(get_project())


def get_project_folder():
    project = get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "library"),
        entity_type="Folder"
    )


def test_project_folder():
    assert_entity(get_project_folder())


def get_project_folder_assetbuild():
    project = get_project()
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
    assert_entity(get_project_folder_assetbuild())


def get_project_folder_assetbuild_task():
    project = get_project()
    assetbuild = get_project_folder_assetbuild()

    return utils.mock_entity(
        ("project", project),
        ("parent", assetbuild),
        ("name", "lookdev"),
        entity_type="Task"
    )


def test_project_folder_assetbuild_task():
    assert_entity(get_project_folder_assetbuild_task())


def get_project_folder_assetbuild_task_workfiles():
    project = get_project()
    parent = get_project_folder_assetbuild()
    return generate_work_file_tasks(parent, project, "lookdev", "Lookdev")


def test_project_folder_assetbuild_task_workfiles():
    for entity in get_project_folder_assetbuild_task_workfiles():
        assert_entity(entity)


def get_project_folder_assetbuild_task_file_components():
    task = get_project_folder_assetbuild_task()
    return generate_file_components(task)


def test_project_folder_assetbuild_task_file_components():
    for entity in get_project_folder_assetbuild_task_file_components():
        assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_components():
    task = get_project_folder_assetbuild_task()
    return generate_sequence_components(task)


def test_project_folder_assetbuild_task_sequence_components():
    for entity in get_project_folder_assetbuild_task_sequence_components():
        assert_entity(entity)


def get_project_folder_assetbuild_task_sequence_files():
    return generate_container_members(
        get_project_folder_assetbuild_task_sequence_components()
    )


def test_project_folder_assetbuild_task_sequence_files():
    e = get_project_folder_assetbuild_task_sequence_files()
    for entity in e:
        assert_entity(entity)


def get_project_task():
    project = get_project()
    return utils.mock_entity(
        ("parent", project),
        ("project", project),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_task():
    assert_entity(get_project_task())


def get_project_task_workfiles():
    project = get_project()
    return generate_work_file_tasks(project, project, "editing", "Editing")


def test_project_task_workfiles():
    for entity in get_project_task_workfiles():
        assert_entity(entity)


def get_project_task_file_components():
    task = get_project_task()
    return generate_file_components(task)


def test_project_task_file_components():
    for entity in get_project_task_file_components():
        assert_entity(entity)


def get_project_task_sequence_components():
    task = get_project_task()
    return generate_sequence_components(task)


def test_project_task_sequence_components():
    for entity in get_project_task_sequence_components():
        assert_entity(entity)


def get_project_task_sequence_files():
    return generate_container_members(
        get_project_task_sequence_components()
    )


def test_project_task_sequence_files():
    for entity in get_project_task_sequence_files():
        assert_entity(entity)


def get_project_shot():
    project = get_project()

    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_shot():
    assert_entity(get_project_shot())


def get_project_shot_task():
    project = get_project()
    parent = get_project_shot()

    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "animation"),
        entity_type="Task"
    )


def test_project_shot_task():
    assert_entity(get_project_shot_task())


def get_project_shot_task_workfiles():
    project = get_project()
    parent = get_project_shot()
    return generate_work_file_tasks(parent, project, "animation", "Animation")


def test_project_shot_task_workfiles():
    for entity in get_project_shot_task_workfiles():
        assert_entity(entity)


def get_project_shot_task_file_components():
    task = get_project_shot_task()
    return generate_file_components(task)


def test_project_shot_task_file_components():
    for entity in get_project_shot_task_file_components():
        assert_entity(entity)


def get_project_shot_task_sequence_components():
    task = get_project_shot_task()
    return generate_sequence_components(task)


def test_project_shot_task_sequence_components():
    for entity in get_project_shot_task_sequence_components():
        assert_entity(entity)


def get_project_shot_task_sequence_files():
    return generate_container_members(
        get_project_shot_task_sequence_components()
    )


def test_project_shot_task_sequence_files():
    for entity in get_project_shot_task_sequence_files():
        assert_entity(entity)


def get_project_sequence():
    project = get_project()
    return utils.mock_entity(
        ("project", project),
        ("parent", project),
        ("name", "sq001"),
        entity_type="Sequence"
    )


def test_project_sequence():
    assert_entity(get_project_sequence())


def get_project_sequence_task():
    project = get_project()
    parent = get_project_sequence()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "editing"),
        entity_type="Task"
    )


def test_project_sequence_task():
    assert_entity(get_project_sequence_task())


def get_project_sequence_task_workfiles():
    project = get_project()
    parent = get_project_sequence()
    return generate_work_file_tasks(parent, project, "editing", "Editing")


def test_project_sequence_task_workfiles():
    for entity in get_project_sequence_task_workfiles():
        assert_entity(entity)


def get_project_sequence_task_file_components():
    task = get_project_sequence_task()
    return generate_file_components(task)


def test_project_sequence_task_file_components():
    for entity in get_project_sequence_task_file_components():
        assert_entity(entity)


def get_project_sequence_task_sequence_components():
    task = get_project_sequence_task()
    return generate_sequence_components(task)


def test_project_sequence_task_sequence_components():
    for entity in get_project_sequence_task_sequence_components():
        assert_entity(entity)


def get_project_sequence_task_sequence_files():
    return generate_container_members(
        get_project_sequence_task_sequence_components()
    )


def test_project_sequence_task_sequence_files():
    for entity in get_project_sequence_task_sequence_files():
        assert_entity(entity)


def get_project_sequence_shot():
    project = get_project()
    parent = get_project_sequence()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "sh0010"),
        entity_type="Shot"
    )


def test_project_sequence_shot():
    assert_entity(get_project_sequence_shot())


def get_project_sequence_shot_task():
    project = get_project()
    parent = get_project_sequence_shot()
    return utils.mock_entity(
        ("project", project),
        ("parent", parent),
        ("name", "compositing"),
        entity_type="Task"
    )


def test_project_sequence_shot_task():
    assert_entity(get_project_sequence_shot_task())


def get_project_sequence_shot_task_workfiles():
    project = get_project()
    parent = get_project_sequence_shot()
    return generate_work_file_tasks(
        parent, project, "compositing", "Compositing"
    )


def test_project_sequence_shot_task_workfiles():
    for entity in get_project_sequence_shot_task_workfiles():
        assert_entity(entity)


def get_project_sequence_shot_task_file_components():
    task = get_project_sequence_shot_task()
    return generate_file_components(task)


def test_project_sequence_shot_task_file_components():
    for entity in get_project_sequence_shot_task_file_components():
        assert_entity(entity)


def get_project_sequence_shot_task_sequence_components():
    task = get_project_sequence_shot_task()
    return generate_sequence_components(task)


def test_project_sequence_shot_task_sequence_components():
    for entity in get_project_sequence_shot_task_sequence_components():
        assert_entity(entity)


def get_project_sequence_shot_task_sequence_files():
    return generate_container_members(
        get_project_sequence_shot_task_sequence_components()
    )


def test_project_sequence_shot_task_sequence_files():
    for entity in get_project_sequence_shot_task_sequence_files():
        assert_entity(entity)


def get_entities():
    entities = []

    entities.append(get_project())

    entities.append(get_project_task())
    entities.extend(get_project_task_workfiles())
    entities.extend(get_project_task_file_components())
    entities.extend(get_project_task_sequence_components())
    entities.extend(get_project_task_sequence_files())

    entities.append(get_project_folder())
    entities.append(get_project_folder_assetbuild())
    entities.append(get_project_folder_assetbuild_task())
    entities.extend(get_project_folder_assetbuild_task_workfiles())
    entities.extend(get_project_folder_assetbuild_task_file_components())
    entities.extend(get_project_folder_assetbuild_task_sequence_components())
    entities.extend(
        get_project_folder_assetbuild_task_sequence_files()
    )

    entities.append(get_project_shot())
    entities.append(get_project_shot_task())
    entities.extend(get_project_shot_task_workfiles())
    entities.extend(get_project_shot_task_file_components())
    entities.extend(get_project_shot_task_sequence_components())
    entities.extend(get_project_shot_task_sequence_files())

    entities.append(get_project_sequence())
    entities.append(get_project_sequence_task())
    entities.extend(get_project_sequence_task_workfiles())
    entities.extend(get_project_sequence_task_file_components())
    entities.extend(get_project_sequence_task_sequence_components())
    entities.extend(
        get_project_sequence_task_sequence_files()
    )

    entities.append(get_project_sequence_shot())
    entities.append(get_project_sequence_shot_task())
    entities.extend(get_project_sequence_shot_task_workfiles())
    entities.extend(get_project_sequence_shot_task_file_components())
    entities.extend(get_project_sequence_shot_task_sequence_components())
    entities.extend(
        get_project_sequence_shot_task_sequence_files()
    )

    return entities
