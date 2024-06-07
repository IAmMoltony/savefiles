import shutil
import subprocess
import os

def open_file(file):
    if hasattr(os, "startfile"): # If startfile is available, use that
        os.startfile(file)
        return True
    if shutil.which("xdg-open"): # If the command has XDG open, open the file with that
        subprocess.call(["xdg-open", file])
        return True
    if "EDITOR" in os.environ: # If $EDITOR is set, use it
        subprocess.call([os.environ["EDITOR"], file])
        return True

    return False # No way of opening file found
