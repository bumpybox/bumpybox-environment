import sys

import maya.standalone

maya.standalone.initialize(name='python')

import maya.cmds as mc

path = sys.argv[1]

print "Saving workfile to: \"{0}\"".format(path)
mc.file(rename=path)
mc.file(save=True, force=True, type="mayaBinary")
