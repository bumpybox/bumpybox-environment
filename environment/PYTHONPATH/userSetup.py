from functools import partial

import pymel.core as pm
import maya.cmds as cmds


# Marking menu
WindowName = 'CustomAnimationMarkingMenu'


PositionNorth = 'N'
PositionNorthEast = 'NE'
PositionNorthWest = 'NW'
PositionEast = 'E'
PositionSouth = 'S'
PositionSouthEast = 'SE'
PositionSouthWest = 'SW'
PositionWest = 'W'

MouseButtonMiddle = 2


def resetAttribute(node, attr):

    # Reset attributes to default if keyable
    if cmds.attributeQuery(attr, node=node, keyable=True):
        values = cmds.attributeQuery(attr, node=node, listDefault=True)

        try:
            cmds.setAttr(node + '.' + attr, *values)
        except:
            pass


def resetAttributes(node, translation=True, rotation=True,
                    scale=True, userAttrs=True):

    if translation:
        resetAttribute(node, 'tx')
        resetAttribute(node, 'ty')
        resetAttribute(node, 'tz')

    if rotation:
        resetAttribute(node, 'rx')
        resetAttribute(node, 'ry')
        resetAttribute(node, 'rz')

    if scale:
        resetAttribute(node, 'sx')
        resetAttribute(node, 'sy')
        resetAttribute(node, 'sz')

    if userAttrs:
        if cmds.listAttr(node, userDefined=True):
            for attr in cmds.listAttr(node, userDefined=True):
                resetAttribute(node, attr)


def resetSelection(translation=True, rotation=True,
                   scale=True, userAttrs=True):

    # Undo enable
    cmds.undoInfo(openChunk=True)

    # Getting selection
    sel = cmds.ls(sl=True)

    # Zero nodes
    if len(sel) >= 1:
        for node in cmds.ls(sl=True):
            resetAttributes(
                node, translation, rotation, scale, userAttrs
            )

        # Revert selection
        cmds.select(sel)
    else:
        cmds.warning('No nodes select!')

    cmds.undoInfo(closeChunk=True)


def get_all_nodes(node_list):
    namespaces = []
    for node in node_list:
        namespace = ":".join(node.name().split(":")[:-1])
        if namespace not in namespaces:
            namespaces.append(namespace)

    sets = [x + ":controls_SET" for x in namespaces]
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
    pm.select(node_list[1], node_list[0])
    import Red9.core.Red9_AnimationUtils as r9Anim
    r9Anim.AnimFunctions.snap()
    pm.select(node_list)


def zv_attach_cmd(node_list, *args):
    from tapp.maya.utils import ZvParentMaster
    ZvParentMaster.attach()


def zv_detach_cmd(node_list, *args):
    from tapp.maya.utils import ZvParentMaster
    ZvParentMaster.detach()


def zv_destroy_cmd(node_list, *args):
    from tapp.maya.utils import ZvParentMaster
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
            l='Select All',
            c=partial(
                select_all_cmd,
                selection
            ),
            rp=PositionNorthWest,
            p=WindowName
        )

        # Key all
        pm.menuItem(
            l='Key All',
            c=partial(
                key_all_cmd,
                selection
            ),
            rp=PositionWest,
            p=WindowName
        )

        # Reset all
        pm.menuItem(
            l='Reset All',
            c=partial(
                reset_all_cmd,
                selection
            ),
            rp=PositionSouthWest,
            p=WindowName
        )

        # zv detach
        pm.menuItem(
            l='zv detach',
            c=partial(
                zv_detach_cmd,
                selection
            ),
            rp=PositionSouth,
            p=WindowName
        )

        # zv destroy
        pm.menuItem(
            l='zv destroy',
            c=partial(
                zv_destroy_cmd,
                selection
            ),
            rp=PositionSouthEast,
            p=WindowName
        )

        if selection_count >= 2:
            # Align
            pm.menuItem(
                l='Align',
                c=partial(
                    align_cmd,
                    selection
                ),
                rp=PositionNorth,
                p=WindowName
            )
            # zv attach
            pm.menuItem(
                l='zv attach',
                c=partial(
                    zv_attach_cmd,
                    selection
                ),
                rp=PositionNorthEast,
                p=WindowName
            )

    else:
        print 'Window doesnt exist : ' % WindowName


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
        p='viewPanes',
        pmc=pre_command
    )


pm.evalDeferred("main()")
pm.evalDeferred(
    "from bumpybox_environment.maya import shelves;shelves.create()"
)
