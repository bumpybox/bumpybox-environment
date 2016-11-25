import os
import subprocess
import sys
import re

"""
func = os.path.dirname
#env_root = func(sys.executable)
repo_root = os.path.join(os.path.dirname(__file__))

# Install PySide for ftrack-connect.
if not conda_git_deployment.utils.check_module("PySide"):
    subprocess.call(["pip", "install", "PySide"])

# Check for ftrack_connect module and install if missing.
cwd = os.path.join(repo_root, "submodules", "ftrack-connect")
# Currently reset to older release because of maya issues.
subprocess.call(["git", "reset", "--hard", "0.1.25"], cwd=cwd)
if not conda_git_deployment.utils.check_module("ftrack_connect"):
    subprocess.call(["python", "setup.py", "install"], cwd=cwd)

# Check for ftrack_connect_maya module and install if missing.
cwd = os.path.join(repo_root, "submodules", "ftrack-connect-maya")
# Currently reset to older release because of https://bitbucket.org/ftrack/ftrack-connect-maya/pull-requests/22/check-maya-version-to-decide-which-way-to/diff#comment-None
subprocess.call(["git", "reset", "--hard", "0.2.3"], cwd=cwd)
if not conda_git_deployment.utils.check_module("ftrack_connect_maya"):
    subprocess.call(["python", "setup.py", "install"], cwd=cwd)

# The "ftrack" module is required for the install of ftrack-connect-nuke.
path = os.path.join(repo_root, "environment", "PYTHONPATH")
try:
    os.environ["PYTHONPATH"] += os.pathsep + path
except:
    os.environ["PYTHONPATH"] = path

# Check for ftrack_connect_nuke module and install if missing.
cwd = os.path.join(repo_root, "submodules", "ftrack-connect-nuke")
if not conda_git_deployment.utils.check_module("ftrack_connect_nuke"):
    subprocess.call(["python", "setup.py", "install"], cwd=cwd)
"""
repo_root = os.path.join(os.path.dirname(__file__))

pythonpath = [
    os.path.join(repo_root, "environment", "PYTHONPATH")
]
# Conda modifies the sys.path, so any application expecting python modules to
# be in PYTHONPATH needs to be added manually. This is usually egg paths.
for path in sys.path:
    if path.endswith(".egg"):
        pythonpath.append(path)

# Adding hook directories for ftrack-connect to pick up actions.
import ftrack_connect_maya
# To import ftrack_connect_nuke, the ftrack module is required to be available.
sys.path.append(os.path.join(repo_root, "environment", "PYTHONPATH"))
import ftrack_connect_nuke

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
