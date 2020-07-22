from functools import partial

import pymel.core as pm
import maya.cmds as cmds

import ZvParentMaster


# Marking menu
WindowName = "CustomAnimationMarkingMenu"


PositionNorth = "N"
PositionNorthEast = "NE"
PositionNorthWest = "NW"
PositionEast = "E"
PositionSouth = "S"
PositionSouthEast = "SE"
PositionSouthWest = "SW"
PositionWest = "W"

MouseButtonMiddle = 2


def resetAttribute(node, attr):

    # Reset attributes to default if keyable
    if cmds.attributeQuery(attr, node=node, keyable=True):
        values = cmds.attributeQuery(attr, node=node, listDefault=True)

        try:
            cmds.setAttr(node + "." + attr, *values)
        except Exception:
            pass


def resetAttributes(node, translation=True, rotation=True,
                    scale=True, userAttrs=True):

    if translation:
        resetAttribute(node, "tx")
        resetAttribute(node, "ty")
        resetAttribute(node, "tz")

    if rotation:
        resetAttribute(node, "rx")
        resetAttribute(node, "ry")
        resetAttribute(node, "rz")

    if scale:
        resetAttribute(node, "sx")
        resetAttribute(node, "sy")
        resetAttribute(node, "sz")

    if userAttrs:
        if cmds.listAttr(node, userDefined=True):
            for attr in cmds.listAttr(node, userDefined=True):
                resetAttribute(node, attr)


def resetSelection(translation=True, rotation=True,
                   scale=True, userAttrs=True):

    # Undo enable
    cmds.undoInfo(openChunk=True)

    # Getting selection
    sel = cmds.ls(selection=True)

    # Zero nodes
    if len(sel) >= 1:
        for node in cmds.ls(selection=True):
            resetAttributes(
                node, translation, rotation, scale, userAttrs
            )

        # Revert selection
        cmds.select(sel)
    else:
        cmds.warning("No nodes select!")

    cmds.undoInfo(closeChunk=True)


def get_all_nodes(node_list):
    namespaces = []
    for node in node_list:
        namespace = ":".join(node.name().split(":")[:-1])
        if namespace not in namespaces:
            namespaces.append(namespace)

    controls = []
    for set in [x + ":controls_SET" for x in namespaces]:
        controls.extend(pm.PyNode(set).members())

    return controls


def select_all(node_list):
    pm.select(get_all_nodes(node_list))


def reset_all_cmd(node_list, *args):
    nodes = get_all_nodes(node_list)
    selection_nodes = nodes
    for node in nodes:
        if "world" in node.name():
            selection_nodes.remove(node)
    pm.select(selection_nodes)
    resetSelection()


def key_all_cmd(node_list, *args):
    select_all(node_list)
    pm.setKeyframe()


def select_all_cmd(node_list, *args):
    select_all(node_list)


def align_cmd(node_list, *args):
    pm.matchTransform(node_list[0], node_list[1])


def zv_attach_cmd(node_list, *args):
    ZvParentMaster.attach()


def zv_detach_cmd(node_list, *args):
    ZvParentMaster.detach()


def zv_destroy_cmd(node_list, *args):
    ZvParentMaster.destroy()


def pre_command(*args):
    if pm.popupMenu(WindowName, ex=True):
        # Clear existing items for the wrapped commands, or we
        # could just edit them
        pm.popupMenu(WindowName, e=True, deleteAllItems=True)
        pm.setParent(WindowName, menu=True)

        # Context sensitive
        selection = pm.selected()
        selection_count = len(selection)

        # Dont re-build if we have nothing selected
        if not selection_count:
            return

        # Select all
        pm.menuItem(
            label="Select All",
            command=partial(select_all_cmd, selection),
            radialPosition=PositionNorthWest,
            parent=WindowName
        )

        # Key all
        pm.menuItem(
            label="Key All",
            command=partial(key_all_cmd, selection),
            radialPosition=PositionWest,
            parent=WindowName
        )

        # Reset all
        pm.menuItem(
            label="Reset All",
            command=partial(reset_all_cmd, selection),
            radialPosition=PositionSouthWest,
            parent=WindowName
        )

        # zv detach
        pm.menuItem(
            label="zv detach",
            command=partial(zv_detach_cmd, selection),
            radialPosition=PositionSouth,
            parent=WindowName
        )

        # zv destroy
        pm.menuItem(
            label="zv destroy",
            command=partial(zv_destroy_cmd, selection),
            radialPosition=PositionSouthEast,
            parent=WindowName
        )

        if selection_count >= 2:
            # Align
            pm.menuItem(
                label="Align",
                command=partial(align_cmd, selection),
                radialPosition=PositionNorth,
                parent=WindowName
            )
            # zv attach
            pm.menuItem(
                label="zv attach",
                command=partial(zv_attach_cmd, selection),
                radialPosition=PositionNorthEast,
                parent=WindowName
            )

    else:
        print("Window doesnt exist : {}".format(WindowName))


def fix_incompatible_instances():
    mapping = {
        "endFrame": "frameEnd",
        "startFrame": "frameStart"
    }

    objectset = cmds.ls("*.id", long=True, type="objectSet",
                        recursive=True, objectsOnly=True)

    for objset in objectset:
        if not cmds.attributeQuery("id", node=objset, exists=True):
            continue

        id_attr = "{}.id".format(objset)
        if cmds.getAttr(id_attr) != "pyblish.avalon.instance":
            continue

        attributes = cmds.listAttr(objset)
        for key, value in mapping.iteritems():
            if key not in attributes:
                continue

            attribute = "{}.{}".format(objset, key)
            print("Changing {} to {}.".format(attribute, value))
            cmds.renameAttr(attribute, value)


def on_open(*args, **kwargs):
    fix_incompatible_instances()


def main():
    if pm.popupMenu(WindowName, ex=True):
        pm.deleteUI(WindowName)

    pm.popupMenu(
        WindowName,
        ctl=True,
        sh=True,
        alt=False,
        b=MouseButtonMiddle,
        mm=True,
        p="viewPanes",
        pmc=pre_command
    )


try:
    import avalon
    avalon.api.on("open", on_open)
except ImportError:
    pass

pm.evalDeferred("main()")
pm.evalDeferred(
    "from bumpybox_environment.maya import shelves;shelves.create()"
)
