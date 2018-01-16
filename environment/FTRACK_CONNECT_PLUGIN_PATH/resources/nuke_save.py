import sys

import nuke


path = sys.argv[1]

print "Saving workfile to: \"{0}\"".format(path)
nuke.scriptSaveAs(path)
