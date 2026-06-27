from fastapi import WebSocket

clients = {}

async def connect(name: str, ws: WebSocket):
    await ws.accept()

    if name not in clients:
        clients[name] = []

    clients[name].append(ws)

async def disconnect(name: str, ws: WebSocket):
    if name in clients:
        if ws in clients[name]:
            clients[name].remove(ws)

async def broadcast(name: str, message: str):
    if name not in clients:
        return

    dead = []

    for ws in clients[name]:
        try:
            await ws.send_text(message)
        except:
            dead.append(ws)

    for ws in dead:
        clients[name].remove(ws)
