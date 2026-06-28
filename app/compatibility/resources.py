from fastapi import APIRouter

from app.process.monitor import stats

router = APIRouter()


@router.get("/servers/{name}/resources")
def resources(name: str):
    s = stats(name)

    return {
        "current_state": "running" if s.get("running") else "offline",
        "is_suspended": False,

        "resources": {
            "memory_bytes": int(s.get("memory_mb", 0) * 1024 * 1024),
            "cpu_absolute": s.get("cpu", 0.0),
            "disk_bytes": 0,
            "network_rx_bytes": 0,
            "network_tx_bytes": 0,
            "uptime": s.get("uptime", 0),
        }
    }
