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
        image="pythonFamily.png",
        imageOverlayLabel="CAI",
        annotation="Create animation instances.",
        label="Create Animation Instances",
        command="from bumpybox_environment.maya import setup;"
        "setup.animation_create()"
    )

    cmds.shelfTabLayout(gShelfTopLevel, edit=True, selectTab=shelfName)
