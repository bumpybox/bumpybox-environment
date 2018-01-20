import os
import requests
import zipfile

import psutil

from conda_git_deployment import utils


def download_file(url, path):
    r = requests.get(url, stream=True)
    with open(path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024):
            if chunk:
                f.write(chunk)
    if os.path.exists(path):
        return True
    else:
        return False


# Install DJV
root = os.path.dirname(__file__)
applications_path = os.path.join(root, "applications")
application_path = os.path.join(applications_path, "djv-1.1.0-Windows-64")

if not os.path.exists(applications_path):
    os.makedirs(applications_path)

path = os.path.join(applications_path, "djv.zip")

if not os.path.exists(application_path) and not os.path.exists(path):
    print "Installing DJV..."
    url = "https://downloads.sourceforge.net/project/djv/djv-stable/1.1.0/"
    url += "djv-1.1.0-Windows-64.zip"
    download_file(url, path)

    zip_ref = zipfile.ZipFile(path, "r")
    zip_ref.extractall(applications_path)
    zip_ref.close()

    os.remove(path)

# Setup environment
environment = {}

# PATH
environment["PATH"] = [
    os.path.abspath(
        os.path.join(
            __file__, "..", "applications", "djv-1.1.0-Windows-64", "bin"
        )
    )
]

# PYTHONPATH
environment["PYTHONPATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-maya",
        "pyblish_maya",
        "pythonpath"
    ),
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-nukestudio"),
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
    os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
    os.path.join(os.path.dirname(__file__), "environment", "PYTHONPATH"),
]

# LUCIDITY_TEMPLATE_PATH
environment["LUCIDITY_TEMPLATE_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "LUCIDITY_TEMPLATE_PATH"
    ),
]

# HIERO_PLUGIN_PATH
environment["HIERO_PLUGIN_PATH"] = [
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-nukestudio",
        "pyblish_nukestudio",
        "hiero_plugin_path",
    ),
    os.path.join(
        os.environ["CONDA_GIT_REPOSITORY"],
        "pyblish-grill-environment",
        "environment",
        "HIERO_PLUGIN_PATH"
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
        os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "create_structure"
    ),
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_CONNECT_PLUGIN_PATH"
    )
]

# FTRACK_EVENT_PLUGIN_PATH
environment["FTRACK_EVENT_PLUGIN_PATH"] = [
    os.path.join(
        os.path.dirname(__file__), "environment", "FTRACK_EVENT_PLUGIN_PATH"
    )
]

# PYBLISH_HOTKEY
environment["PYBLISH_HOTKEY"] = ["Ctrl+Alt+P"]

# PYBLISH_QML_MODAL
environment["PYBLISH_QML_MODAL"] = ["True"]

# Kill existing ftrack_connects
for proc in psutil.process_iter():
    try:
        if "ftrack_connect" in proc.cmdline():
            proc.kill()
    except psutil.AccessDenied:
        # Some process does not allow you to get "cmdline()"
        pass

utils.write_environment(environment)
