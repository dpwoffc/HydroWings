import psutil
import time
from app.process.runner import processes

def stats(name):
    if name not in processes:
        return {"running": False}

    proc = processes[name]

    if proc.poll() is not None:
        return {"running": False}

    p = psutil.Process(proc.pid)

    return {
        "running": True,
        "pid": proc.pid,
        "cpu": p.cpu_percent(interval=0.1),
        "memory_mb": round(p.memory_info().rss / 1024 / 1024, 2),
        "threads": p.num_threads(),
        "uptime": round(time.time() - p.create_time())
    }
