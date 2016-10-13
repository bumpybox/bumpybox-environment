import subprocess

# install git and update
subprocess.call(["conda", "install", "-c", "anaconda", "git", "-y"])
subprocess.call(["git", "pull"])
subprocess.call(["git", "submodule", "update", "--init", "--recursive"])
subprocess.call(["git", "submodule", "update", "--recursive"])
