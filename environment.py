import os
import subprocess
import sys
import re

import conda_git_deployment.utils
import ftrack_connect_maya


func = os.path.dirname
#env_root = func(sys.executable)
repo_root = os.path.join(os.path.dirname(__file__))

pythonpath = [
    os.path.join(repo_root, "environment", "PYTHONPATH")
]
# Conda modifies the sys.path, so any application expecting python modules to
# be in PYTHONPATH needs to be added manually. This is usually egg paths.
for path in sys.path:
    if path.endswith(".egg"):
        pythonpath.append(path)

ftrack_connect_plugin_path = [
    os.path.abspath(
        os.path.join(os.path.dirname(ftrack_connect_maya.__file__), "..")
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

# launch
subprocess.call(["python", "-m", "ftrack_connect"])
