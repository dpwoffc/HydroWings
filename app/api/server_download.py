from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import FileResponse

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.get("/api/servers/{uuid}/files/download")
async def download(uuid: str, file: str):
    path = ROOT / uuid / file.lstrip("/")

    return FileResponse(
        path,
        filename=path.name,
    )
