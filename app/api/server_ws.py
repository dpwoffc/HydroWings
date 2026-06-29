from fastapi import APIRouter, WebSocket

router = APIRouter()

@router.websocket("/api/servers/{uuid}/ws")
async def ws(websocket: WebSocket, uuid: str):
    await websocket.accept()

    await websocket.send_json({
        "event": "console output",
        "args": ["HydroWings WS Connected\n"]
    })

    while True:
        msg = await websocket.receive_text()

        await websocket.send_json({
            "event": "console output",
            "args": [f"> {msg}\n"]
        })
