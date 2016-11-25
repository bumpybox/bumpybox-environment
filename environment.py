import os
import subprocess
import sys
import re

import conda_git_deployment.utils
import ftrack_connect_maya
import ftrack_connect_nuke


repo_root = os.path.join(os.path.dirname(__file__))

pythonpath = [
    os.path.abspath(
        os.path.join(repo_root, "submodules", "pyblish-base")
    ),
]
# Conda modifies the sys.path, so any application expecting python modules to
# be in PYTHONPATH needs to be added manually. This is usually egg paths.
for path in sys.path:
    if path.endswith(".egg"):
        pythonpath.append(path)

# Adding hook directories for ftrack-connect to pick up actions.
ftrack_connect_plugin_path = [
    os.path.abspath(
        os.path.join(os.path.dirname(ftrack_connect_maya.__file__), "..")
    ),
    os.path.abspath(
        os.path.join(os.path.dirname(ftrack_connect_nuke.__file__), "..")
    )
]

# Setting environment.
env = {
    "PYTHONPATH": pythonpath,
    "FTRACK_CONNECT_PLUGIN_PATH": ftrack_connect_plugin_path,
}
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
