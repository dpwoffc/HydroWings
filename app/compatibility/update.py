from fastapi import APIRouter, Body

from app.config.config import save

router = APIRouter()


@router.post("/api/update")
def update(config: dict = Body(...)):
    save(config)

    print("=" * 60)
    print("CONFIG UPDATED")
    print(config)
    print("=" * 60)

    return {
        "success": True
    }
