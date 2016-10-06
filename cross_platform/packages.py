import sys
import os
import subprocess


env_root = os.path.dirname(sys.executable)

# install PySide
src = os.path.join(env_root, "Lib", "site-packages", "PySide")
if os.path.exists(src):
    print "Skipping existing module: \"PySide\""
else:
    subprocess.call(["pip", "install", "PySide"])
