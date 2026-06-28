from fastapi import APIRouter
from pathlib import Path

router = APIRouter()

VERSION = Path("VERSION").read_text().strip()

@router.get("/system")
def system():
    return {
        "name": "HydroWings",
        "version": VERSION,
        "api": 1,
        "docker": False,
        "platform": "Android"
    }
