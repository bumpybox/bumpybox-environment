import maya.cmds as cmds
import maya.mel as mel


def create():

    # BUMPYBOX shelf
    shelfName = "Bumpybox"
    if cmds.shelfLayout(shelfName, exists=True):
        cmds.deleteUI(shelfName)

    mel.eval("global string $gShelfTopLevel")
    gShelfTopLevel = mel.eval("$temp = $gShelfTopLevel")
    if gShelfTopLevel:
        shelf = cmds.shelfLayout(
            shelfName, parent=gShelfTopLevel, style="iconAndTextHorizontal"
        )
    else:
        shelf = cmds.shelfLayout(shelfName, style="iconAndTextHorizontal")

    cmds.shelfButton(
        parent=shelf,
        image="studio_library.png",
        label="Studio Library",
        annotation="Studio Library",
        command="import studiolibrary;studiolibrary.main()"
    )

    cmds.shelfButton(
        parent=shelf,
        image="pythonFamily.png",
        imageOverlayLabel="LIP",
        annotation="Select the image plane, and execute.",
        label="Localize Image Plane",
        command="""import os
import shutil

import pymel.core


image_plane = pymel.core.ls(selection=True)[0]
src = image_plane.imageName.get()
dst = os.path.join(os.path.expanduser('~'), os.path.basename(src))
shutil.copy(src, dst)
image_plane.imageName.set(dst)
try:
    image_plane.addAttr("remoteImageName", dt="string")
except:
    pass
image_plane.remoteImageName.set(src)""",
    )

    cmds.shelfButton(
        parent=shelf,
        image="pythonFamily.png",
        imageOverlayLabel="UIP",
        annotation="Select image plane and execute.",
        label="Unlocalize Image Plane",
        command="""import os
import shutil

import pymel.core


image_plane = pymel.core.ls(selection=True)[0]
image_plane.imageName.set(image_plane.remoteImageName.get())""",
    )

    cmds.shelfButton(
        parent=shelf,
        label="Import Rigging",
        image="pythonFamily.png",
        imageOverlayLabel="IR",
        annotation="Import all linked rigs.",
        command="from bumpybox_environment.maya import setup;"
        "setup.import_rigging()"
    )

    cmds.shelfButton(
        parent=shelf,
        label="Import Movie (Full)",
        image="pythonFamily.png",
        imageOverlayLabel="IM(F)",
        annotation="Import full resolution movie.",
        command="from bumpybox_environment.maya import setup;"
        "setup.import_full_resolution_movie()"
    )

    cmds.shelfButton(
        parent=shelf,
        label="Import Movie (Half)",
        image="pythonFamily.png",
        imageOverlayLabel="IM(H)",
        annotation="Import half resolution movie.",
        command="from bumpybox_environment.maya import setup;"
        "setup.import_half_resolution_movie()"
    )

    cmds.shelfButton(
        parent=shelf,
        label="Import Tracking",
        image="pythonFamily.png",
        imageOverlayLabel="IT",
        annotation="Import tracking.",
        command="from bumpybox_environment.maya import setup;"
        "setup.import_tracking()"
    )

    cmds.shelfButton(
        parent=shelf,
        label="Import Audio",
        image="pythonFamily.png",
        imageOverlayLabel="IA",
        annotation="Import audio.",
        command="from bumpybox_environment.maya import setup;"
        "setup.import_audio()"
    )

    cmds.shelfTabLayout(gShelfTopLevel, edit=True, selectTab=shelfName)
