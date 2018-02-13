import os
import operator

import maya.cmds as cmds
import pymel

import ftrack_api
import ftrack_connect
from ftrack_connect.connector import FTAssetObject
from ftrack_connect_maya.connector import Connector


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

    import_components(
        [latest_component],
        {
            "attachCamera": True,
            "renameCamera": False,
            "resolutionGate": True,
            "imagePlaneVisibility": "Hidden from other cameras",
            "createGround": False,
            "imagePlaneDepth": 10000
        }
    )


def import_half_resolution_movie():

    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    # Import Imageplane
    components = session.query(
        "Component where version.asset.name is \"editing_half_resolution\" "
        "and version.asset.parent.id is \"{0}\"".format(task["parent"]["id"])
    )

    latest_component = get_latest_component(components)

    if not latest_component:
        return

    import_components(
        [latest_component],
        {
            "attachCamera": True,
            "renameCamera": False,
            "resolutionGate": True,
            "imagePlaneVisibility": "Hidden from other cameras",
            "createGround": False,
            "imagePlaneDepth": 10000
        }
    )


def get_latest_component(components):
    max_version = 0
    latest_component = None
    for component in components:
        if max_version < component["version"]["version"]:
            max_version = component["version"]["version"]
            latest_component = component

    return latest_component


def get_latest_components(components):
    data = {}
    for component in components:
        data[component["version"]["version"]] = []
    for component in components:
        data[component["version"]["version"]].append(component)

    return data[max(data.keys())]


def import_rigging():
    """Imports rigging from linked AssetBuilds."""

    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    links = session.query(
        "select from_id from TypedContextLink where to_id is "
        "\"{0}\"".format(task["parent"]["id"])
    )
    for link in links:
        components = session.query(
            "Component where version.task.type.name is \"Rigging\" and "
            "version.asset.type.short is \"scene\" and "
            "version.asset.parent.id is \"{0}\"".format(link["from_id"])
        )

        latest_component = get_latest_component(components)

        if not latest_component:
            continue

        import_components(
            [latest_component],
            {
                "mayaAddNamespace": True,
                "mayaNamespace": "Custom",
                "nameSpaceStr": "{0}_rig".format(
                    latest_component["version"]["asset"]["parent"]["name"]
                ),
                "mayaGroupNodes": False
            }
        )


def import_tracking():
    session = ftrack_connect.session.get_shared_session()

    components = session.query(
        "Component where version.task.type.name is \"Tracking\" and "
        "version.asset.type.short is \"cache\""
    )
    import_components(
        get_latest_components(components),
        {
            "mayaNamespace": True,
            "nameSpaceStr": "tracking",
            "mayaTimeline": False,
            "connectSelection": False
        }
    )


def import_audio():
    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    components = session.query(
        "Component where version.asset.type.short is \"audio\" "
        "and version.asset.parent.id is \"{0}\"".format(task["parent"]["id"])
    )

    import_components(get_latest_components(components))


def import_animation():
    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    components = session.query(
        "Component where version.task.type.name is \"Animation\" and "
        "version.asset.type.short is \"cache\" and "
        "version.asset.parent.id is \"{0}\"".format(task["parent"]["id"])
    )

    import_components(
        get_latest_components(components),
        {
            "mayaNamespace": True,
            "nameSpaceStr": "animation",
            "mayaTimeline": False,
            "connectSelection": False
        }
    )


def import_lookdev():
    """Imports lookdev from linked AssetBuilds."""

    session = ftrack_connect.session.get_shared_session()
    task = session.get("Task", os.environ["FTRACK_TASKID"])

    links = session.query(
        "select from_id from TypedContextLink where to_id is "
        "\"{0}\"".format(task["parent"]["id"])
    )
    for link in links:
        components = session.query(
            "Component where version.task.type.name is \"Lookdev\" and "
            "version.asset.type.short is \"scene\" and "
            "version.asset.parent.id is \"{0}\"".format(link["from_id"])
        )

        component = get_latest_components(components)[0]

        if not component:
            continue

        import_components(
            [component],
            {
                "mayaAddNamespace": True,
                "mayaNamespace": "Custom",
                "nameSpaceStr": "{0}_lookdev".format(
                    component["version"]["asset"]["parent"]["name"]
                ),
                "mayaGroupNodes": False
            }
        )


def connect_alembic():

    data = {}
    for node in pymel.core.ls(type="mesh", uuid=True):
        uuid = None
        source = False
        try:
            uuid = node.uuid.get()
            source = True
        except AttributeError:
            uuid = cmds.ls(node.name(), uuid=True)[0]

        node_data = data.get(uuid, {})
        if source:
            node_data["source"] = node
        else:
            node_data["destination"] = node

        data[uuid] = node_data

    for uuid, uuid_data in data.iteritems():

        if "source" not in uuid_data:
            continue

        if "destination" not in uuid_data:
            continue

        pymel.core.blendShape(
            uuid_data["source"],
            uuid_data["destination"],
            weight=[(0, 1)],
            origin="world"
        )
