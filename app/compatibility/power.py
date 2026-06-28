from fastapi import APIRouter

from pydantic import BaseModel

from app.process.runner import start_server
from app.process.runner import stop_server
from app.process.restart import restart_server

from app.server_manager import get_server
from app.core.runtime import build_command

router = APIRouter()


class Signal(BaseModel):

    signal: str


@router.post("/servers/{uuid}/power")

def power(uuid: str, req: Signal):

    server = get_server(uuid)

    if server is None:

        return {"error": "server not found"}

    if req.signal == "start":

        return start_server(

            uuid,

            f"instances/{uuid}",

            build_command(server["runtime"], server["entry"])

        )

    elif req.signal == "stop":

        return stop_server(uuid)

    elif req.signal == "restart":

        return restart_server(uuid)

    return {

        "error": "unknown signal"

    }
