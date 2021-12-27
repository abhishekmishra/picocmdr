from SciFiCmdr import commander
import os
import sys
from pathlib import Path

from SciFiCmdr.SciFiCmdr import register_command, register_handler


def list_dir_get_executables(directory):
    directory = os.path.abspath(directory)
    execfiles = []
    if os.path.exists(directory) and os.path.isdir(directory):
        onlyfiles = [
            f
            for f in os.listdir(directory)
            if os.path.isfile(os.path.join(directory, f))
        ]
        for f in onlyfiles:
            if sys.platform == "win32":
                fp = Path(f)
                if fp.suffix.lower() in [
                    ".bat",
                    ".cmd",
                    ".com",
                    ".exe",
                    ".ps1",
                ]:
                    execfiles.append(f)
            else:
                if os.access(f, os.X_OK):
                    execfiles.append(f)
        return execfiles
    return execfiles


def run():
    env_path = os.environ.get("PATH", None)
    if env_path is not None and len(env_path) > 0:
        paths = env_path.split(os.pathsep)
        print(paths)
        for p in paths:
            execfiles = list_dir_get_executables(p)
            for e in execfiles:
                try:
                    cmdname = Path(e).name
                    register_command(cmdname)
                    register_handler(cmdname, lambda: os.system(e))
                except KeyError as ke:
                    print(ke)

    command = commander(title="PicoCmdr")
    if command is not None and len(command) > 0:
        os.system(command)
