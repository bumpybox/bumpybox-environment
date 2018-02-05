import os

import lucidity

import lib
import test_project_templates as tpt
import test_project_shot_templates as tpst
import test_project_folder_templates as tpft
import test_project_episode_templates as tpet


def get_test_paths():
    return [
        "//disk/test_project",
        "//disk/test_project/in",
        "//disk/test_project/out",

        "//disk/test_project/publish",

        "//disk/test_project/publish/library",
        "//disk/test_project/publish/library/character/characterA",
        "//disk/test_project/publish/library/character/characterA/lookdev",

        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/characterA_lookdev_v0001.mb",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/characterA_lookdev_v0001.nk",

        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001.mb",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001.abc",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001.mov",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001.wav",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001.gizmo",

        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001/"
        "characterA_lookdev_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/library/character/characterA/lookdev/"
        "v0001/output/characterA_lookdev_instanceName_v0001/"
        "characterA_lookdev_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/tasks/editing/v0001/"
        "editing_v0001.hrox",

        "//disk/test_project/publish/shots/sh0010",
        "//disk/test_project/publish/shots/sh0010/lighting",

        "//disk/test_project/publish/shots/sh0010/lighting/v0001/"
        "sh0010_lighting_v0001.mb",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/"
        "sh0010_lighting_v0001.nk",

        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001.mb",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001.abc",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001.mov",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001.wav",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001.gizmo",

        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001/"
        "sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/shots/sh0010/lighting/v0001/output/"
        "sh0010_lighting_instanceName_v0001/"
        "sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/publish/episodes/ep0010",

        "//disk/test_project/publish/episodes/ep0010/editing",
        "//disk/test_project/publish/episodes/ep0010/editing/v0001/"
        "ep0010_editing_v0001.hrox",

        "//disk/test_project/publish/episodes/ep0010/sh0010",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting",

        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/ep0010_sh0010_lighting_v0001.mb",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/ep0010_sh0010_lighting_v0001.nk",

        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/"
        "ep0010_sh0010_lighting_instanceName_v0001.mb",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/"
        "ep0010_sh0010_lighting_instanceName_v0001.abc",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/"
        "ep0010_sh0010_lighting_instanceName_v0001.mov",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/"
        "ep0010_sh0010_lighting_instanceName_v0001.wav",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/"
        "ep0010_sh0010_lighting_instanceName_v0001.gizmo",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/ep0010_sh0010_lighting_instanceName_v0001/"
        "ep0010_sh0010_lighting_instanceName_v0001.%04d.exr",
        "//disk/test_project/publish/episodes/ep0010/sh0010/lighting/"
        "v0001/output/ep0010_sh0010_lighting_instanceName_v0001/"
        "ep0010_sh0010_lighting_instanceName_v0001.1001.exr",

        "//disk/test_project/work",

        "//disk/test_project/work/library",
        "//disk/test_project/work/library/character/characterA",
        "//disk/test_project/work/library/character/characterA/lookdev",
        "//disk/test_project/work/library/character/characterA/lookdev/"
        "characterA_lookdev_v0001.mb",
        "//disk/test_project/work/library/character/characterA/lookdev/"
        "characterA_lookdev_v0001.nk",

        "//disk/test_project/work/tasks/editing",
        "//disk/test_project/work/tasks/editing/editing_v0001.hrox",

        "//disk/test_project/work/shots/sh0010",
        "//disk/test_project/work/shots/sh0010/lighting",
        "//disk/test_project/work/shots/sh0010/lighting/"
        "sh0010_lighting_v0001.mb",
        "//disk/test_project/work/shots/sh0010/lighting/"
        "sh0010_lighting_v0001.nk",

        "//disk/test_project/work/episodes/ep0010",

        "//disk/test_project/work/episodes/ep0010/editing",
        "//disk/test_project/work/episodes/ep0010/editing/"
        "ep0010_editing_v0001.hrox",

        "//disk/test_project/work/episodes/ep0010/sh0010",
        "//disk/test_project/work/episodes/ep0010/sh0010/lighting",
        "//disk/test_project/work/episodes/ep0010/sh0010/lighting/"
        "ep0010_sh0010_lighting_v0001.mb",
        "//disk/test_project/work/episodes/ep0010/sh0010/lighting/"
        "ep0010_sh0010_lighting_v0001.nk",
    ]


def test_environment():
    msg = "Could not find \"LUCIDITY_TEMPLATE_PATH\" in environment."
    assert "LUCIDITY_TEMPLATE_PATH" in os.environ.keys(), msg


def test_templates_existence():
    templates = lucidity.discover_templates()
    assert templates, "No templates discovered."


def test_proposed_paths():
    template_paths = []
    for entity in get_entities():
        template_paths.extend(lib.get_resolved_paths(entity))

    paths = get_test_paths()
    for path in template_paths:
        if path in paths:
            paths.remove(path)

    msg = "Paths not covered by templates:"
    for path in sorted(paths):
        msg += "\n{0}".format(path)
    msg += "\nTemplate paths:"
    for path in sorted(template_paths):
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
        template_paths.extend(lib.get_resolved_paths(entity))

    # Cover excess templates
    paths = []
    for path in template_paths:
        if path not in get_test_paths():
            paths.append(path)

    msg = "Excess template paths:"
    for path in paths:
        msg += "\n{0}".format(path)
    assert not paths, msg


def get_entities():
    entities = []

    entities.extend(tpt.get_entities())
    entities.extend(tpft.get_entities())
    entities.extend(tpst.get_entities())
    entities.extend(tpet.get_entities())

    return entities
