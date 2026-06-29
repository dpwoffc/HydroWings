from pathlib import Path

from fastapi import APIRouter

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.get("/api/servers/{uuid}/files/contents")
async def contents(uuid: str, file: str):
    path = ROOT / uuid / file.lstrip("/")

    if not path.exists():
        return ""

    return path.read_text(errors="ignore")
