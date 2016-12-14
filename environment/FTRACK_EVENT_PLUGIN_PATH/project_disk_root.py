import os

import ftrack_api
import ftrack_template


class Structure(ftrack_api.structure.base.Structure):

    def get_resource_identifier(self, entity, context=None):

        templates = ftrack_template.discover_templates()

        path = ftrack_template.format(
            {}, templates, entity=entity
        )[0].replace("\\", "/").replace("//", "/")

        if entity.entity_type == "SequenceComponent":

            padding = entity["padding"]
            if padding:
                expression = "%0{0}d".format(padding)
            else:
                expression = "%d"

            filetype = entity["file_type"]
            path = path.replace(
                filetype, "/{0}.{1}{2}".format(
                    os.path.splitext(os.path.basename(path))[0],
                    expression,
                    filetype
                )
            )

        return path


def configure_locations(event):
    """Configure locations for session."""
    session = event["data"]["session"]

    # Find location(s) and customise instances.
    location = session.query(
        "Location where name is \"project.disk.root\""
    ).one()
    ftrack_api.mixin(
        location, ftrack_api.entity.location.UnmanagedLocationMixin
    )
    location.accessor = ftrack_api.accessor.disk.DiskAccessor(prefix="")
    location.structure = Structure()
    location.priority = 50
    print location


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
