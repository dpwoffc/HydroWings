from pathlib import Path
from zipfile import ZipFile

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/decompress")
async def extract(uuid: str, body: dict = Body(...)):
    archive = ROOT / uuid / body["root"].lstrip("/") / body["file"]

    with ZipFile(archive, "r") as z:
        z.extractall(archive.parent)

    return {
        "success": True
    }
