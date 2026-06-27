from fastapi import FastAPI
from pydantic import BaseModel
from app.server_manager import list_servers
from app.server_manager import get_server
from app.core.runtime import build_command

from pathlib import Path

banner = Path("assets/banner.txt")

if banner.exists():
    print(banner.read_text())

from app.process.runner import (
    start_server,
    stop_server,
    status,
    get_logs
)

app = FastAPI(
    title="HydroWings",
    version="0.1.0-alpha"
)


class StartRequest(BaseModel):
    name: str
    cwd: str
    cmd: str


@app.get("/")
def root():
    return {
    "daemon": "HydroWings",
    "version": "0.1.0-alpha",
    "status": "online",
    "platform": "Android"
}


@app.get("/servers")
def servers():
    return list_servers()


@app.get("/servers/logs/{name}")
def logs(name: str):
    return get_logs(name)


@app.post("/servers/start")
def start(req: StartRequest):
    return start_server(
        req.name,
        req.cwd,
        req.cmd
    )


@app.post("/servers/stop/{name}")
def stop(name: str):
    return stop_server(name)

from fastapi import WebSocket
from app.ws.events import connect, disconnect


@app.websocket("/console/{name}")
async def console(ws: WebSocket, name: str):

    await connect(name, ws)

    try:
        while True:
            await ws.receive_text()

    except:
        await disconnect(name, ws)

@app.post("/servers/{name}/start")
def start_named(name: str):

    server = get_server(name)

    if server is None:
        return {"error": "server not found"}

    cmd = build_command(
        server["runtime"],
        server["entry"]
    )

    if cmd is None:
        return {"error": "unsupported runtime"}

    return start_server(
        name=name,
        cwd=f"instances/{name}",
        cmd=cmd
    )

@app.post("/servers/{name}/stop")
def stop_named(name: str):
    return stop_server(name)
