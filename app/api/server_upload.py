from pathlib import Path

from fastapi import APIRouter, UploadFile, File

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/upload")
async def upload(uuid: str, files: list[UploadFile] = File(...)):
    base = ROOT / uuid

    for f in files:
        data = await f.read()
        (base / f.filename).write_bytes(data)

    return {"success": True}
