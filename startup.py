import os
import subprocess
import sys

repo_root = os.path.join(os.path.dirname(__file__))

env = {}

# PYTHONPATH
paths = [
    os.path.join(repo_root, "environment", "PYTHONPATH"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-base"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-lite"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-maya"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-maya",
                 "pyblish_maya", "pythonpath"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "environment_variables", "pythonpath"),
]
# Conda modifies the sys.path, so any application expecting python modules to
# be in PYTHONPATH needs to be added manually. This is usually egg paths.
for path in sys.path:
    if path.endswith(".egg"):
        paths.append(path)

env["PYTHONPATH"] = paths

# NUKE_PATH
paths = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "nuke_path"),
]

env["NUKE_PATH"] = paths

# HOUDINI_PATH
paths = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "houdini_path"),
    "&"
]

env["HOUDINI_PATH"] = paths

# HIERO_PLUGIN_PATH
paths = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "hiero_plugin_path"),
]

env["HIERO_PLUGIN_PATH"] = paths

# PYBLISHPLUGINPATH
paths = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins", "maya"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins", "houdini"),
]

env["PYBLISHPLUGINPATH"] = paths

# FTRACK_CONNECT_PLUGIN_PATH
# Adding hook directories for ftrack-connect to pick up actions.
import ftrack_connect_maya

ftrack_connect_plugin_path = [
    os.path.abspath(
        os.path.join(os.path.dirname(ftrack_connect_maya.__file__), "..")
    ),
    os.path.join(repo_root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
]
env["FTRACK_CONNECT_PLUGIN_PATH"] = ftrack_connect_plugin_path

# Setting environment.
for variable in env:
    path = ""
    for item in env[variable]:
        path += os.pathsep + item

    try:
        os.environ[variable] += path
    except:
        os.environ[variable] = path

# Launch ftrack-connect
subprocess.call(["python", "-m", "ftrack_connect"])
