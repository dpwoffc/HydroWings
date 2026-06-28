import asyncio
import json

clients = {}

async def connect(server, ws):
    if server not in clients:
        clients[server] = set()

    clients[server].add(ws)


async def disconnect(server, ws):
    if server in clients:
        clients[server].discard(ws)


async def emit(server, event, args=None):
    if args is None:
        args = []

    payload = json.dumps({
        "event": event,
        "args": args
    })

    dead = []

    for ws in clients.get(server, set()):
        try:
            await ws.send_text(payload)
        except:
            dead.append(ws)

    for ws in dead:
        clients[server].discard(ws)
