import os

import ftrack_api


def modify_launch(event):
    """Modify the application environment to include new api location."""

    data = event["data"]

    data["options"]["env"]["FTRACK_EVENT_PLUGIN_PATH"] = (
        os.path.join(
            os.environ["CONDA_GIT_REPOSITORY"],
            "bumpybox-environment",
            "environment",
            "FTRACK_EVENT_PLUGIN_PATH"
        ) + os.pathsep +
        data["options"]["env"].get("FTRACK_EVENT_PLUGIN_PATH", "")
    )

    return data


def register(session, **kw):
    '''Register event listener.'''

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = "topic=ftrack.connect.application.launch"
    session.event_hub.subscribe(subscription, modify_launch)
