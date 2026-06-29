from pathlib import Path

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/rename")
async def rename(uuid: str, body: list = Body(...)):
    for item in body:
        old = ROOT / uuid / item["from"].lstrip("/")
        new = ROOT / uuid / item["to"].lstrip("/")

        new.parent.mkdir(parents=True, exist_ok=True)

        if old.exists():
            old.rename(new)

    return {"success": True}
