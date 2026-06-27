from app.process.runner import stop_server, start_server
from app.server_manager import get_server
from app.core.runtime import build_command

def restart_server(name: str):
    server = get_server(name)

    if server is None:
        return {"error": "server not found"}

    stop_server(name)

    cmd = build_command(
        server["runtime"],
        server["entry"]
    )

    return start_server(
        name=name,
        cwd=f"instances/{name}",
        cmd=cmd
    )
