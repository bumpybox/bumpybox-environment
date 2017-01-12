import ftrack
import ftrack_locations


def register(registry, **kw):

    # Validate that registry is the correct ftrack.Registry. If not,
    # assume that register is being called with another purpose or from a
    # new or incompatible API and return without doing anything.
    if registry is not ftrack.LOCATION_PLUGINS:
        # Exit to avoid registering this plugin again.
        return

    location = ftrack_locations.get_old_location()

    registry.add(location)
