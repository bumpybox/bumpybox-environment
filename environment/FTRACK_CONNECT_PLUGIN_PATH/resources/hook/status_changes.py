import getpass

import ftrack_api
from ftrack_connect.session import get_shared_session


def callback(event):
    """Status change updates."""

    session = get_shared_session()

    for entity_data in event["data"].get("entities", []):

        if entity_data["action"] != "update":
            continue

        if "keys" not in entity_data:
            continue

        if "statusid" not in entity_data["keys"]:
            continue

        new_status = session.get(
            "Status", entity_data["changes"]["statusid"]["new"]
        )

        # AssetVersion changes
        if entity_data["entityType"] == "assetversion":
            entity = session.get("AssetVersion", entity_data["entityId"])

            if new_status["name"] == "Pending Changes":
                entity["task"]["status"] = new_status

            if new_status["name"] == "Internal Approved":
                entity["task"]["status"] = new_status

            if new_status["name"] == "External Review":
                entity["task"]["status"] = new_status

            if new_status["name"] == "External Approved":
                entity["task"]["status"] = new_status

    session.commit()


def register(session, **kw):
    """Register event listener."""

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = (
        "topic=ftrack.update and source.applicationId=ftrack.client.web and "
        "source.user.username={0}".format(getpass.getuser())
    )
    session.event_hub.subscribe(subscription, callback)
