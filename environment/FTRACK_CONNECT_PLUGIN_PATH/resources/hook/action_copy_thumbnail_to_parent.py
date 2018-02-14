import ftrack_api
from ftrack_hooks.action import BaseAction


class ActionCopyThumbnailToParent(BaseAction):
    label = "Copy Thumbnail To Parent"
    variant = None
    identifier = "copy-thumbnail-to-parent"
    description = None

    def __init__(self, session):
        """Expects a ftrack_api.Session instance"""
        super(ActionCopyThumbnailToParent, self).__init__(session)

    def discover(self, session, entities, event):

        # Only discover the action if any selection is made.
        if entities:
            return True

        return False

    def launch(self, session, entities, event):

        for entity in entities:
            task = session.get("Task", entity[1])
            task["parent"]["thumbnail_id"] = task["thumbnail_id"]

        session.commit()

        return {
            "success": True,
            "message": "Thumbnails copied!",
        }


def register(session):

    # Validate that session is an instance of ftrack_api.Session. If not,assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    # Create action and register to respond to discover and launch actions.
    action = ActionCopyThumbnailToParent(session)
    action.register()
