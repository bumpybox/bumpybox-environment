import ftrack_api
import ftrack_locations


def configure_locations(event):
    """Configure locations for session."""
    session = event["data"]["session"]

    # Find location(s) and customise instances.
    location = ftrack_locations.get_new_location(session)
    ftrack_api.mixin(
        location, ftrack_api.entity.location.UnmanagedLocationMixin
    )


def register(session):
    # Validate that session is an instance of ftrack_api.Session. If not,
    # assume that register is being called from an old or incompatible API and
    # return without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    session.event_hub.subscribe(
        "topic=ftrack.api.session.configure-location",
        configure_locations
    )
