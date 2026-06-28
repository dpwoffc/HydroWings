from fastapi import APIRouter, Body

router = APIRouter()

@router.post("/api/update")
def update(config: dict = Body(...)):
    print("=" * 60)
    print("CONFIG UPDATE FROM PANEL")
    print(config)
    print("=" * 60)

    return {
        "success": True
    }
