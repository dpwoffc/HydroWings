from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

VERSION = Path("VERSION").read_text().strip()


@router.get("/")
def root():
    return {
        "daemon": "HydroWings",
        "version": VERSION,
        "status": "online",
        "platform": "Android",
    }


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/api/system")
def api_system():
    return {
        "name": "HydroWings",
        "version": VERSION,
        "api": 1,
        "platform": "Android",
        "docker": False,
    }
