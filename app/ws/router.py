from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import asyncio

from app.ws.events import connect, disconnect
from app.ws.send import emit
from app.ws.stats import stats_loop
from app.ws.token import verify
from app.process.runner import send_command

router = APIRouter()


@router.websocket("/ws/servers/{uuid}")
async def ws(websocket: WebSocket, uuid: str):

    token = websocket.query_params.get("token")

    if not verify(uuid, token):
        await websocket.close(code=1008)
        return

    await websocket.accept()

    await connect(uuid, websocket)

    await emit(uuid, "auth success", [])

    asyncio.create_task(stats_loop(uuid))

    try:
        while True:

            msg = await websocket.receive_json()

            if msg.get("event") == "send command":

                await asyncio.to_thread(
                    send_command,
                    uuid,
                    msg["args"][0]
                )

    except WebSocketDisconnect:
        pass

    finally:
        await disconnect(uuid, websocket)
