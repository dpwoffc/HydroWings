from pathlib import Path
from zipfile import ZipFile

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/compress")
async def compress(uuid: str, body: dict = Body(...)):
    base = ROOT / uuid

    archive = base / body["name"]

    with ZipFile(archive, "w") as z:
        for file in body["files"]:
            p = base / file
            if p.is_file():
                z.write(p, p.relative_to(base))

    return {
        "success": True
    }
