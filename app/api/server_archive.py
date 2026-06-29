from pathlib import Path
from zipfile import ZipFile

from fastapi import APIRouter

router = APIRouter()

ROOT = Path("app/runtime/servers")
ARCHIVES = Path("app/runtime/archives")


@router.post("/api/servers/{uuid}/archive")
async def archive(uuid: str):
    server = ROOT / uuid

    ARCHIVES.mkdir(parents=True, exist_ok=True)

    archive = ARCHIVES / f"{uuid}.zip"

    with ZipFile(archive, "w") as z:
        for f in server.rglob("*"):
            if f.is_file():
                z.write(f, f.relative_to(server))

    return {
        "success": True,
        "file": archive.name,
    }
