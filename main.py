from pathlib import Path
import asyncio
from contextlib import asynccontextmanager
from fastapi import UploadFile, File
from app.files.upload import upload_zip
from fastapi import Depends, FastAPI, WebSocket
from pydantic import BaseModel
from app.process.runner import send_command
from app.process.restart import restart_server
from app.process.kill import kill_server

from app.auth.token import verify_token
from app.core.runtime import build_command
from app.files.manager import (
    list_files,
    read_file,
    write_file,
    mkdir,
    delete,
)
from app.process.monitor import stats
from app.process.runner import (
    start_server,
    stop_server,
    get_logs,
)
from app.process.supervisor import supervisor
from app.server_manager import (
    list_servers,
    get_server,
)
from app.ws.events import (
    connect,
    disconnect,
)


VERSION = Path("VERSION").read_text().strip()

banner = Path("assets/banner.txt")
if banner.exists():
    print(banner.read_text())


@asynccontextmanager
async def lifespan(app: FastAPI):
    asyncio.create_task(supervisor())
    yield


app = FastAPI(
    title="HydroWings",
    version=VERSION,
    lifespan=lifespan,
)


class ConsoleCommand(BaseModel):
    command: str


class StartRequest(BaseModel):
    name: str
    cwd: str
    cmd: str


class FileWrite(BaseModel):
    path: str
    content: str


class FilePath(BaseModel):
    path: str


@app.get("/")
def root():
    return {
        "daemon": "HydroWings",
        "version": VERSION,
        "status": "online",
        "platform": "Android",
    }


@app.get("/servers")
def servers(_: str = Depends(verify_token)):
    return list_servers()


@app.get("/servers/logs/{name}")
def logs(name: str, _: str = Depends(verify_token)):
    return get_logs(name)


@app.post("/servers/start")
def start(req: StartRequest, _: str = Depends(verify_token)):
    return start_server(
        req.name,
        req.cwd,
        req.cmd,
    )


@app.post("/servers/stop/{name}")
def stop(name: str, _: str = Depends(verify_token)):
    return stop_server(name)


@app.websocket("/console/{name}")
async def console(ws: WebSocket, name: str):
    await connect(name, ws)

    try:
        while True:
            await ws.receive_text()
    except Exception:
        await disconnect(name, ws)


@app.post("/servers/{name}/start")
def start_named(name: str, _: str = Depends(verify_token)):
    server = get_server(name)

    if server is None:
        return {"error": "server not found"}

    cmd = build_command(
        server["runtime"],
        server["entry"],
    )

    if cmd is None:
        return {"error": "unsupported runtime"}

    return start_server(
        name=name,
        cwd=f"instances/{name}",
        cmd=cmd,
    )


@app.post("/servers/{name}/stop")
def stop_named(name: str, _: str = Depends(verify_token)):
    return stop_server(name)


@app.get("/servers/{name}/files")
def files(name: str, _: str = Depends(verify_token)):
    return list_files(name)


@app.get("/servers/{name}/files/read")
def read(name: str, path: str, _: str = Depends(verify_token)):
    return {
        "content": read_file(name, path)
    }


@app.post("/servers/{name}/files/write")
def write(name: str, req: FileWrite, _: str = Depends(verify_token)):
    return write_file(
        name,
        req.path,
        req.content,
    )


@app.post("/servers/{name}/files/mkdir")
def make_dir(name: str, req: FilePath, _: str = Depends(verify_token)):
    return mkdir(name, req.path)


@app.delete("/servers/{name}/files/delete")
def remove(name: str, path: str, _: str = Depends(verify_token)):
    return delete(name, path)


@app.get("/servers/{name}/stats")
def server_stats(name: str, _: str = Depends(verify_token)):
    return stats(name)


@app.post("/servers/{name}/upload")
def upload(
    name: str,
    file: UploadFile = File(...),
    _: str = Depends(verify_token),
):
    return upload_zip(name, file)


@app.post("/servers/{name}/command")
def console_command(
    name: str,
    req: ConsoleCommand,
    _: str = Depends(verify_token)
):
    return send_command(
        name,
        req.command
    )


@app.post("/servers/{name}/restart")
def restart(
    name: str,
    _: str = Depends(verify_token)
):
    return restart_server(name)


@app.post("/servers/{name}/kill")
def kill(
    name: str,
    _: str = Depends(verify_token)
):
    return kill_server(name)


@app.get("/api/system")
def api_system():
    return {
        "name": "HydroWings",
        "version": VERSION,
        "api": 1,
        "platform": "Android",
        "docker": False,
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


@app.get("/servers/{name}")
def server_info(
    name: str,
    _: str = Depends(verify_token)
):
    server = get_server(name)

    if server is None:
        return {"error": "server not found"}

    return server
