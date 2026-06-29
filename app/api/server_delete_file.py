from pathlib import Path
import shutil

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/delete")
async def delete(uuid: str, body: dict = Body(...)):
    for name in body["files"]:
        path = ROOT / uuid / name.lstrip("/")

        if path.is_dir():
            shutil.rmtree(path, ignore_errors=True)

        elif path.exists():
            path.unlink()

    return {"success": True}
