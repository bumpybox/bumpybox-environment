import ftrack_api
from ftrack_connect.session import get_shared_session


def application_launch(event):
    """Return each entities in the selection in data dictionaries."""

    items = []
    for item in event["data"]["selection"]:
        # Add assetversion from thumbnail
        entity = get_shared_session().get("TypedContext", item["entityId"])
        assetversion = get_shared_session().query(
            "select version.id from Component where id is "
            "\"{0}\"".format(entity["thumbnail_id"])
        ).one()["version"]
        items.append(
            {"entityId": assetversion["id"], "entityType": "assetversion"}
        )

    event["data"]["selection"] = items

    return event


def register(session, **kw):
    """Register event listener."""

    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an incompatible API
    # and return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        # Exit to avoid registering this plugin again.
        return

    # Register the event handler
    subscription = "topic=rv.launch"
    session.event_hub.subscribe(subscription, application_launch)
