import os
import subprocess

import config


func = os.path.dirname
repo_root = os.path.join(func(func(__file__)))

# setup environment
for item in os.listdir(os.path.join(repo_root, "environment")):
    try:
        os.environ[item] += os.pathsep
        os.environ[item] += os.path.join(repo_root, "environment", item)
    except:
        os.environ[item] = os.path.join(repo_root, "environment", item)

os.environ["FTRACK_SERVER"] = config.FTRACK_SERVER
os.environ["FTRACK_APIKEY"] = config.FTRACK_APIKEY

env = {"PYTHONPATH": [os.path.join(repo_root, "src", "ftrack-connect",
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

# chaining launch
subprocess.call(["python", os.path.join(repo_root, "utils", "launch.py")])
