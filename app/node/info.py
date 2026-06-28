import os
import time
import platform

from app.server_manager import list_servers
from app.process.runner import processes

BOOT_TIME = time.time()


def heartbeat():
    servers = list_servers()

    running = 0

    for proc in processes.values():
        if proc.poll() is None:
            running += 1

    return {
        "status": "online",
        "version": "0.1.0-alpha",
        "platform": "Android",
        "servers": len(servers),
        "running": running,
        "uptime": int(time.time() - BOOT_TIME),
    }


def info():
    return {
        "hostname": platform.node(),
        "os": platform.system(),
        "release": platform.release(),
        "arch": platform.machine(),
        "python": platform.python_version(),
        "cores": os.cpu_count(),
    }
