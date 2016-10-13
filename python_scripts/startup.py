import os
import subprocess
import sys
import re

import utils


func = os.path.dirname
env_root = func(sys.executable)
repo_root = os.path.join(func(func(__file__)))

# install PySide for ftrack-connect
if not utils.check_module("PySide"):
    subprocess.call(["pip", "install", "PySide"])

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

try:
    import config
    os.environ["FTRACK_SERVER"] = config.FTRACK_SERVER
    os.environ["FTRACK_APIKEY"] = config.FTRACK_APIKEY
except:
    pass

env = {"PYTHONPATH": [os.path.join(repo_root, "src", "Qt.py"),
                      os.path.join(repo_root, "src", "qtext", "source"),
                      os.path.join(repo_root, "src", "ftrack-python-api",
                                   "source"),
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
