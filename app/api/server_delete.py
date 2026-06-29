from pathlib import Path
import shutil

from fastapi import APIRouter, HTTPException

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.delete("/api/servers/{uuid}")
async def delete_server(uuid: str):
    server = ROOT / uuid

    if not server.exists():
        raise HTTPException(404, "Server not found")

    shutil.rmtree(server)

    print("=" * 60)
    print("SERVER DELETED:", uuid)
    print("=" * 60)

    return {"success": True}
