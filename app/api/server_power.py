import json
from pathlib import Path

from fastapi import APIRouter, Body

from app.runtime.process import start, stop

router = APIRouter()

ROOT = Path("app/runtime/servers")

@router.post("/api/servers/{uuid}/power")
async def power(uuid: str, body: dict = Body(...)):
    signal = body["signal"]

    server = ROOT / uuid
    cfg = json.loads((server / "server.json").read_text())

    if signal == "start":
        await start(
            uuid,
            cfg.get("startup", "sleep infinity"),
            str(server),
        )
        state = "running"

    elif signal == "stop":
        await stop(uuid)
        state = "offline"

    else:
        state = "offline"

    (server / "state.json").write_text(json.dumps({
        "state": state,
        "last_action": signal,
    }, indent=4))

    return {"success": True}
