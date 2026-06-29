from pathlib import Path

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.put("/api/servers/{uuid}/files/write")
async def write(uuid: str, file: str, body: str = Body(...)):
    path = ROOT / uuid / file.lstrip("/")

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(body)

    return {
        "success": True
    }
