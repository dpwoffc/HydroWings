from fastapi import APIRouter
from app.server_manager import list_servers

router = APIRouter()

@router.get("/servers")
def servers():

    result = []

    for s in list_servers():

        result.append({

            "uuid": s["name"],

            "name": s["name"],

            "state": "offline"

        })

    return result
