import asyncio

from app.process.monitor import stats
from app.ws.send import emit

async def stats_loop(name: str):
    while True:
        try:
            s = stats(name)

            await emit(
                name,
                "stats",
                [{
                    "memory_bytes": int(s.get("memory_mb", 0) * 1024 * 1024),
                    "cpu_absolute": s.get("cpu", 0.0),
                    "disk_bytes": 0,
                    "network_rx_bytes": 0,
                    "network_tx_bytes": 0,
                    "uptime": s.get("uptime", 0),
                }]
            )

            await asyncio.sleep(1)

        except Exception:
            break
