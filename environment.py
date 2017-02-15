import os

from conda_git_deployment import utils


environment = {}

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-template"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-locations"),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-bumpybox",
        "pyblish_bumpybox",
        "environment_variables",
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
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-hiero"),
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
]

# MAYA_PLUG_IN_PATH
environment["MAYA_PLUG_IN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "Tapp",
        "environment",
        "MAYA_PLUG_IN_PATH"
    ),
]

# MAYA_SHELF_PATH
environment["MAYA_SHELF_PATH"] = [
    os.path.join(os.path.dirname(__file__), "environment", "MAYA_SHELF_PATH")
]

# MAYA_MODULE_PATH
environment["MAYA_MODULE_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "cvshapeinverter"),
]

# ARNOLD_PLUGIN_PATH
environment["ARNOLD_PLUGIN_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "ARNOLD_PLUGIN_PATH"
    )
]

# FTRACK_TEMPLATES_PATH
environment["FTRACK_TEMPLATES_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_TEMPLATES_PATH"
    )
]

# FTRACK_CONNECT_PLUGIN_PATH
environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_CONNECT_PLUGIN_PATH"
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "pyblish-ftrack", "pyblish_ftrack"
    ),
]

# FTRACK_LOCATION_PLUGIN_PATH
environment["FTRACK_LOCATION_PLUGIN_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_LOCATION_PLUGIN_PATH"
    ),
]

# FTRACK_LOCATIONS_MODULE
environment["FTRACK_LOCATIONS_MODULE"] = [
    os.environ.get("FTRACK_LOCATIONS_MODULE", "ftrack_template_disk")
]

utils.write_environment(environment)
