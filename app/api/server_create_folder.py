from pathlib import Path

from fastapi import APIRouter, Body

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.post("/api/servers/{uuid}/files/create-folder")
async def create_folder(uuid: str, body: dict = Body(...)):
    directory = body.get("root", "/")
    name = body["name"]

    path = ROOT / uuid / directory.lstrip("/") / name
    path.mkdir(parents=True, exist_ok=True)

    return {"success": True}
