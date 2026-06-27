import asyncio
from app.process.runner import processes, start_server
from app.server_manager import get_server

async def supervisor():

    while True:

        for name in list(processes.keys()):

            proc = processes[name]

            if proc.poll() is None:
                continue

            server = get_server(name)

            if not server:
                continue

            if server.get("restart") != "always":
                continue

            print(f"[Supervisor] Restarting {name}")

            start_server(
                name,
                f"instances/{name}",
                f"python3 {server['entry']}"
            )

        await asyncio.sleep(2)
