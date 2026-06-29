from fastapi import APIRouter

router = APIRouter()


@router.get("/api/servers/{uuid}")
async def server_details(uuid: str):
    return {
        "state": "offline",
        "is_suspended": False,
        "utilization": {
            "memory_bytes": 0,
            "cpu_absolute": 0.0,
            "disk_bytes": 0,
            "network": {
                "rx_bytes": 0,
                "tx_bytes": 0,
            },
            "uptime": 0,
        }
    }
