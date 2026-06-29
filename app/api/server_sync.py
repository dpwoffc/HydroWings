from pathlib import Path
import json

from fastapi import APIRouter, Body, HTTPException

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/sync")
async def sync_server(uuid: str, data: dict = Body(...)):
    server = ROOT / uuid

    if not server.exists():
        raise HTTPException(404, "Server not found")

    (server / "server.json").write_text(
        json.dumps(data, indent=4)
    )

    print("=" * 60)
    print("SERVER SYNC")
    print(uuid)
    print("=" * 60)

    return {"success": True}
