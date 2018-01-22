import os

import ftrack_api
from bumpybox_environment import utils


def modify_launch(event):
    """Modify the Maya launch with project directory"""

    session = ftrack_api.Session()
    task = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )

    work_file = utils.get_work_file(session, task, "maya", 1)
    project_path = os.path.join(os.path.dirname(work_file))

    event["data"]["command"].extend(["-proj", project_path])


def register(session, **kw):
    """Register event listener."""

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = "topic=ftrack.connect.application.launch and "
    subscription += "data.application.identifier=maya*"
    session.event_hub.subscribe(subscription, modify_launch)
