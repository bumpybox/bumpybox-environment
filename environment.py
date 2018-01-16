import os

from conda_git_deployment import utils


environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "Tapp"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "Tapp",
        "environment",
        "PYTHONPATH"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "studio-library"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "maya-capture"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "maya-capture-gui"),
    os.path.join(os.path.dirname(__file__), "environment", "PYTHONPATH"),
]

# HIERO_PLUGIN_PATH
environment["HIERO_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-hiero",
        "pyblish_hiero",
        "hiero_plugin_path",
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "hiero_plugin_path"
    ),
    os.path.join(
        os.path.dirname(__file__), "environment", "HIERO_PLUGIN_PATH"
    ),
]

# NUKE_PATH
environment["NUKE_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nuke",
        "pyblish_nuke",
        "nuke_path"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
        "nuke_path"
    )
]

# MAYA_PLUG_IN_PATH
environment["MAYA_PLUG_IN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "Tapp",
        "environment",
        "MAYA_PLUG_IN_PATH"
    ),
    os.path.join(os.path.dirname(__file__), "environment", "MAYA_PLUG_IN_PATH")
]

# MAYA_SHELF_PATH
environment["MAYA_SHELF_PATH"] = [
    os.path.join(os.path.dirname(__file__), "environment", "MAYA_SHELF_PATH")
]

# MAYA_MODULE_PATH
environment["MAYA_MODULE_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "cvshapeinverter"),
]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "djv_plugin"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "pending_changes"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "status_assign"
    ),
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_CONNECT_PLUGIN_PATH"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-ftrack", "pyblish_ftrack"
    ),
]

# FTRACK_EVENT_PLUGIN_PATH
environment["FTRACK_EVENT_PLUGIN_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_EVENT_PLUGIN_PATH"
    )
]
utils.write_environment(environment)
