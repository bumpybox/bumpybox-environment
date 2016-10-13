import os
import imp


def check_executable(executable):

    def is_exe(fpath):
        return os.path.isfile(fpath) and os.access(fpath, os.X_OK)

    fpath, fname = os.path.split(executable)
    if fpath:
        if is_exe(executable):
            return executable
    else:
        for path in os.environ["PATH"].split(os.pathsep):
            path = path.strip('"')
            exe_file = os.path.join(path, executable)
            if is_exe(exe_file):
                return exe_file
            if is_exe(exe_file + ".exe"):
                return exe_file + ".exe"

    return None


def check_module(module_name):

    try:
        imp.find_module(module_name)
        return True
    except ImportError:
        return False
