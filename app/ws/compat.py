from fastapi import APIRouter

from app.ws.token import create

router = APIRouter()

@router.get("/api/servers/{uuid}/websocket")
def websocket(uuid: str):

    token = create(uuid)

    return {
        "data": {
            "token": token,
            "socket": f"/ws/servers/{uuid}"
        }
    }
