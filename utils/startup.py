import re
import sys
import os
import subprocess

func = os.path.dirname
env_root = func(sys.executable)
repo_root = os.path.join(func(func(__file__)))

# install git and update
subprocess.call(["conda", "install", "-c", "anaconda", "git", "-y"])
subprocess.call(["git", "pull"])
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])
subprocess.call(["git", "submodule", "update", "--recursive"])

# install PySide for ftrack-connect
src = os.path.join(env_root, "Lib", "site-packages", "PySide")
if os.path.exists(src):
    print "Skipping existing module: \"PySide\""
else:
    subprocess.call(["pip", "install", "PySide"])

# installing all submodules
config = subprocess.check_output(["git", "config", "--list"])
pattern = r"submodule.submodules\/(.+)\.url"
for line in config.split("\n"):
    match = re.match(pattern, line)
    if match:

        # get submodule path
        submodule_name = match.groups()[0]
        path = os.path.join(repo_root, "submodules", submodule_name)
        path = path.replace("\\", "/")

        # get submodule current commit
        commit = subprocess.check_output(["git", "rev-parse", "HEAD"],
                                         cwd=path)
        commit = commit.replace("\n", "")

        # clone/update repo
        url = "git+file://" + path + "@" + commit + "#egg=" + submodule_name
        subprocess.call(["pip", "install", "--editable", url], cwd=repo_root)
        path = os.path.join(repo_root, "src", submodule_name, "setup.py")
        subprocess.call(["python", path, "build"], cwd=os.path.dirname(path))

# chaining environment
subprocess.call(["python", os.path.join(repo_root, "utils", "environment.py")])
