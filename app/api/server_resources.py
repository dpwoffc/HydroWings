import time
import psutil

from fastapi import APIRouter

from app.runtime.process import get_process

router = APIRouter()

START = {}


@router.get("/api/servers/{uuid}/resources")
async def resources(uuid: str):
    proc = get_process(uuid)

    if proc is None:
        return {
            "current_state": "offline",
            "is_suspended": False,
            "resources": {
                "memory_bytes": 0,
                "cpu_absolute": 0,
                "disk_bytes": 0,
                "network_rx_bytes": 0,
                "network_tx_bytes": 0,
                "uptime": 0,
            },
        }

    p = psutil.Process(proc.pid)

    START.setdefault(uuid, time.time())

    return {
        "current_state": "running",
        "is_suspended": False,
        "resources": {
            "memory_bytes": p.memory_info().rss,
            "cpu_absolute": p.cpu_percent(),
            "disk_bytes": 0,
            "network_rx_bytes": 0,
            "network_tx_bytes": 0,
            "uptime": int(time.time() - START[uuid]),
        },
    }
