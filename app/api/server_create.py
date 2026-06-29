from pathlib import Path
import json

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers")
async def create_server(data: dict = Body(...)):
    uuid = data["uuid"]

    server_dir = ROOT / uuid
    print("DIR =", server_dir.resolve())

    server_dir.mkdir(parents=True, exist_ok=True)

    with open(server_dir / "server.json", "w") as f:
        json.dump(data, f, indent=4)

    print("=" * 60)
    print("SERVER CREATED:", uuid)
    print("=" * 60)

    return {"success": True}
