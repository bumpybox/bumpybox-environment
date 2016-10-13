import subprocess

import utils

# install git and update
if not utils.check_executable("git"):
    subprocess.call(["conda", "install", "-c", "anaconda", "git", "-y"])

subprocess.call(["git", "pull"])
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])
subprocess.call(["git", "submodule", "update", "--recursive"])
