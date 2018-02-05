import os
import json
import shutil
import threading
import traceback
import logging

import ftrack_api
from ftrack_hooks.action import BaseAction


class ActionFixThumbnail(BaseAction):
    label = "Fix Thumbnail"
    variant = None
    identifier = "fix-thumbnail"
    description = None

    def __init__(self, session):
        """Expects a ftrack_api.Session instance"""
        super(ActionFixThumbnail, self).__init__(session)

    def discover(self, session, entities, event):

        # Only discover the action if any selection is made.
        if entities:
            return True

        return False

    def launch(self, session, entities, event):

        for entity in entities:
            assetversion = session.get("AssetVersion", entity[1])
            component = session.query(
                "Component where version.id is \"{0}\" and "
                "name is \"thumbnail\"".format(entity[1])
            ).one()

            assetversion["asset"]["parent"]["thumbnail_id"] = component["id"]

        session.commit()

        return {
            "success": True,
            "message": "",
        }


def register(session):

    # Validate that session is an instance of ftrack_api.Session. If not,assume
    # that register is being called from an old or incompatible API and return
    # without doing anything.
    if not isinstance(session, ftrack_api.Session):
        return

    # Create action and register to respond to discover and launch actions.
    action = ActionFixThumbnail(session)
    action.register()
