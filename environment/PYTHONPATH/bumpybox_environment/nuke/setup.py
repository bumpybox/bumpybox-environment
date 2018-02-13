import os
import operator

import nuke

import ftrack_api
import ftrack_connect
from ftrack_connect.connector import FTAssetObject
from ftrack_connect_nuke.connector import Connector


def import_components(components, options={}):
    """Import components with host plugins iterator."""

    locations = {}
    session = ftrack_connect.session.get_shared_session()
    for location in session.query("select id from Location"):
        locations[location["id"]] = location

    connector = Connector()
    for component in components:
        try:
            location_id = max(
                component.get_availability().iteritems(),
                key=operator.itemgetter(1)
            )[0]
            file_path = locations[location_id].get_resource_identifier(
                component
            )

            asset = FTAssetObject(
                    componentId=component['id'],
                    filePath=file_path,
                    componentName=component['name'],
                    assetVersionId=component["version"]["id"],
                    options=options
            )

            connector.importAsset(asset)
        except ftrack_api.exception.ComponentNotInLocationError:
            pass


def get_latest_component(components):
    max_version = 0
    latest_component = None
    for component in components:
        if max_version < component["version"]["version"]:
            max_version = component["version"]["version"]
            latest_component = component

    return latest_component


def import_full_resolution_movie():

    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    # Import Imageplane
    components = session.query(
        "Component where version.asset.name is \"editing_full_resolution\" "
        "and version.asset.parent.id is \"{0}\"".format(task["parent"]["id"])
    )

    latest_component = get_latest_component(components)

    if not latest_component:
        return

    path = session.pick_location().get_filesystem_path(
        latest_component
    ).replace("\\", "/")
    duration = (
        nuke.root()["last_frame"].value() - nuke.root()["first_frame"].value()
    )
    node = nuke.createNode('Read', inpanel=False)
    node['file'].setValue(path)
    node["frame_mode"].setValue("start at")
    node["frame"].setValue(str(nuke.root()["first_frame"].value()))
    node["last"].setValue(int(duration) + 1)
    node["origlast"].setValue(int(duration) + 1)
