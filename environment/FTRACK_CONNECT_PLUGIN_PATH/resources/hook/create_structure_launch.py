import os
import shutil

import ftrack_api
from ftrack_connect.session import get_shared_session
import lucidity


def inject_paths(event, entities):

    templates = lucidity.discover_templates()
    event["data"]["files"] = []
    event["data"]["directories"] = []
    for entity in entities:
        valid_templates = templates[0].get_valid_templates(
            entity, templates
        )

        for template in valid_templates:

            try:
                path = os.path.abspath(
                    template.format(entity)
                ).replace("\\", "/")
            except lucidity.error.FormatError:
                continue
            else:
                if hasattr(template, "source"):
                    event["data"]["files"].append((template.source, path))
                else:
                    if os.path.exists(path):
                        continue

                    event["data"]["directories"].append(path)

    return event


def application_launch(event):
    """Return each entities in the selection in data dictionaries."""

    session = get_shared_session()
    entity = session.get(
        "Task", event["data"]["context"]["selection"][0]["entityId"]
    )
    entities = []
    for link in entity["link"]:
        entities.append(session.get(link["type"], link["id"]))

    event = inject_paths(event, entities)

    for path in event["data"]["directories"]:
        os.makedirs(path)

    for src, dst in event["data"]["files"]:
        print "Copying \"{0}\" to \"{1}\"".format(src, dst)

        if not os.path.exists(os.path.dirname(dst)):
            os.makedirs(os.path.dirname(dst))

        shutil.copy(src, dst)


def structure_launch(event):

    return inject_paths(event, event["data"].get("entities", []))


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
    session.event_hub.subscribe(subscription, application_launch)

    subscription = "topic=create_structure.launch"
    session.event_hub.subscribe(subscription, structure_launch)
