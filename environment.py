import os

import psutil

from conda_git_deployment import utils
import environment_setup


def main():
    environment = {}

    # PATH
    environment["PATH"] = [
        os.path.abspath(
            os.path.join(
                __file__, "..", "applications", "djv-1.1.0-Windows-64", "bin"
            )
        ),
        "C:/Program Files (x86)/QuickTime/QTSystem/"
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
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "studiolibrary", ".."
        ),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "maya-capture"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "maya-capture-gui"),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "maya-alembic-export"
        ),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "filelink"),
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "pyblish-bumpybox"),
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
        ),
        os.path.join(
            os.path.dirname(__file__), "environment", "NUKE_PATH"
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
        os.path.join(
            os.path.dirname(__file__), "environment", "MAYA_PLUG_IN_PATH"
        )
    ]

    # XBMLANGPATH
    environment["XBMLANGPATH"] = [
        os.path.join(os.path.dirname(__file__), "environment", "XBMLANGPATH")
    ]

    # MAYA_MODULE_PATH
    environment["MAYA_MODULE_PATH"] = [
        os.path.join(os.environ["CONDA_GIT_REPOSITORY"], "cvshapeinverter"),
    ]

    # ARNOLD_PLUGIN_PATH
    environment["ARNOLD_PLUGIN_PATH"] = [
        os.path.abspath(
            os.path.join(
                __file__,
                "..",
                "applications",
                "alShaders-win-2.0.0b2-ai5.0.1.0",
                "bin"
            )
        )
    ]

    # FTRACK_CONNECT_PLUGIN_PATH
    environment["FTRACK_CONNECT_PLUGIN_PATH"] = [
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"], "ftrack-hooks", "djv_plugin"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "create_structure"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "batch_tasks"
        ),
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "ftrack-hooks",
            "running_jobs"
        ),
        os.path.join(
            os.path.dirname(__file__),
            "environment",
            "FTRACK_CONNECT_PLUGIN_PATH"
        )
    ]

    # FTRACK_EVENT_PLUGIN_PATH
    environment["FTRACK_EVENT_PLUGIN_PATH"] = [
        os.path.join(
            os.path.dirname(__file__),
            "environment",
            "FTRACK_EVENT_PLUGIN_PATH"
        )
    ]

    # PYBLISH_HOTKEY
    environment["PYBLISH_HOTKEY"] = ["Ctrl+Alt+P"]

    # PYBLISH_QML_MODAL
    environment["PYBLISH_QML_MODAL"] = ["True"]

    # PYBLISH_ALLOW_DUPLICATE_PLUGIN_NAMES
    environment["PYBLISH_ALLOW_DUPLICATE_PLUGIN_NAMES"] = ["True"]

    # solidangle_LICENSE
    environment["solidangle_LICENSE"] = ["5053"]

    # foundry_LICENSE
    environment["foundry_LICENSE"] = ["4101@172.17.0.2"]

    # Kill existing ftrack_connects
    for proc in psutil.process_iter():
        try:
            if "ftrack_connect" in proc.cmdline():
                proc.kill()
        except psutil.AccessDenied:
            # Some process does not allow you to get "cmdline()"
            pass

    utils.write_environment(environment)


if __name__ == "__main__":
    environment_setup.install_djv()
    main()
