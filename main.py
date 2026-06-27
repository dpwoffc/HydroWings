from fastapi import FastAPI
from pydantic import BaseModel

from app.process.runner import (
    start_server,
    stop_server,
    status,
    get_logs
)

app = FastAPI(title="DroidDaemon")


class StartRequest(BaseModel):
    name: str
    cwd: str
    cmd: str


@app.get("/")
def root():
    return {
        "daemon": "DroidDaemon",
        "status": "online"
    }


@app.get("/servers")
def servers():
    return status()


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
