from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.get("/api/servers/{uuid}/console")
async def console(uuid: str):
    log = ROOT / uuid / "console.log"

    if not log.exists():
        log.write_text("HydroWings Console Ready\n")

    return {
        "data": log.read_text()
    }
