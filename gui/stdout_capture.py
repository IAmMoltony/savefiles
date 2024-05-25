import sys
import io

def start():
    capture_io = io.StringIO()
    old_stdout = sys.stdout
    sys.stdout = capture_io
    return capture_io, old_stdout

def end(capture_io, old_stdout):
    sys.stdout = old_stdout
    output = capture_io.getvalue()
    capture_io.close()
    return output

