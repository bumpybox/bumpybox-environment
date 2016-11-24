import os
import subprocess
import sys
import re

import conda_git_deployment.utils


func = os.path.dirname
#env_root = func(sys.executable)
repo_root = os.path.join(os.path.dirname(__file__))

# Install PySide for ftrack-connect.
if not conda_git_deployment.utils.check_module("PySide"):
    subprocess.call(["pip", "install", "PySide"])
"""
# installing all submodules
config = subprocess.check_output(["git", "config", "--list"])
pattern = r"submodule.submodules\/(.+)\.url"
setup_files = []
for line in config.split("\n"):
    match = re.match(pattern, line)
    if match:

        # get submodule path
        submodule_name = match.groups()[0]
        path = os.path.join(repo_root, "submodules", submodule_name)
        path = path.replace("\\", "/")

        if not os.path.exists(path):
            continue

        # get submodule current commit
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                         cwd=path)
        commit = commit.replace("\n", "")

        # clone/update repo
        url = "git+file://" + path + "@" + commit + "#egg=" + submodule_name
        subprocess.call(["pip", "install", "--editable", url], cwd=repo_root)

        path = os.path.join(repo_root, "src", submodule_name, "setup.py")
        setup_files.append(path)

# building submodules
for path in setup_files:
    subprocess.call(["python", path, "build"], cwd=os.path.dirname(path))

# setup environment
for item in os.listdir(os.path.join(repo_root, "environment")):
    try:
        os.environ[item] += os.pathsep
        os.environ[item] += os.path.join(repo_root, "environment", item)
    except:
        os.environ[item] = os.path.join(repo_root, "environment", item)

env = {"PYTHONPATH": [os.path.join(repo_root, "src", "Qt.py"),
                      os.path.join(repo_root, "src", "qtext", "source"),
                      os.path.join(repo_root, "src", "ftrack-connect",
                                   "source"),
                      os.path.join(repo_root, "src",
                                   "ftrack-connect-foundry", "source"),
                      os.path.join(repo_root, "src",
                                   "ftrack-connect-maya", "source"),
                      os.path.join(repo_root, "src",
                                   "ftrack-connect-maya", "resource",
                                   "scripts"),
                      os.path.join(repo_root, "src",
                                   "ftrack-connect-nuke", "source")],
       "FTRACK_CONNECT_PLUGIN_PATH": [os.path.join(repo_root, "src",
                                                   "ftrack-connect"),
                                      os.path.join(repo_root, "src",
                                                   "ftrack-connect-foundry"),
                                      os.path.join(repo_root, "src",
                                                   "ftrack-connect-maya"),
                                      os.path.join(repo_root, "src",
                                                   "ftrack-connect-nuke")],
       "FTRACK_CONNECT_NUKE_PLUGINS_PATH": [os.path.join(repo_root,
                                                         "src",
                                                         "ftrack-connect-nuke",
                                                         "resource")],
       "FTRACK_CONNECT_MAYA_PLUGINS_PATH": [os.path.join(repo_root,
                                                         "src",
                                                         "ftrack-connect-maya",
                                                         "resource")]}
"""
cwd = os.path.join(repo_root, "submodules", "ftrack-connect")
subprocess.call(["git", "reset", "--hard", "0.1.25"], cwd=cwd)
if not conda_git_deployment.utils.check_module("ftrack_connect"):
    subprocess.call(["python", "setup.py", "install"], cwd=cwd)

cwd = os.path.join(repo_root, "submodules", "ftrack-connect-maya")
subprocess.call(["git", "reset", "--hard", "0.2.3"], cwd=cwd)
if not conda_git_deployment.utils.check_module("ftrack_connect_maya"):
    subprocess.call(["python", "setup.py", "install"], cwd=cwd)

# launch
subprocess.call(["python", os.path.join(repo_root, "environment.py")])
