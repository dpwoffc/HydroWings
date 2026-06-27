import os
import signal

from app.process.runner import processes

def kill_server(name):

    if name not in processes:
        return {"error":"not running"}

    proc = processes[name]

    os.kill(proc.pid, signal.SIGKILL)

    return {
        "status":"killed"
    }
