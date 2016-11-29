import os
import subprocess


repo_root = os.path.join(os.path.dirname(__file__))
env = {}

# PYTHONPATH
env["PYTHONPATH"] = [
    os.path.join(repo_root, "environment", "PYTHONPATH"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-maya",
                 "pyblish_maya", "pythonpath"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "environment_variables", "pythonpath"),
]

# NUKE_PATH
env["NUKE_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "environment_variables", "nuke_path"),
]

# HOUDINI_PATH
env["HOUDINI_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "environment_variables", "houdini_path"),
    "&"
]

# HIERO_PLUGIN_PATH
env["HIERO_PLUGIN_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "environment_variables",
                 "hiero_plugin_path"),
]

# PYBLISHPLUGINPATH
env["PYBLISHPLUGINPATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins", "maya"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins", "houdini"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox",
                 "pyblish_bumpybox", "plugins", "ftrack"),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-ftrack",
                 "pyblish_ftrack", "plugins"),
]

# FTRACK_CONNECT_PLUGIN_PATH
env["FTRACK_CONNECT_PLUGIN_PATH"] = [
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-connect-maya"),
    os.path.join(repo_root, "environment", "FTRACK_CONNECT_PLUGIN_PATH"),
    #os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
]

# FTRACK_CONNECT_MAYA_PLUGINS_PATH
env["FTRACK_CONNECT_MAYA_PLUGINS_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-connect-maya", "resource"
    )
]

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
