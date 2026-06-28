import asyncio
import subprocess
import threading

import psutil

from app.ws.send import emit

processes = {}
logs = {}


def _reader(name, proc):
    logs[name] = []

    for line in iter(proc.stdout.readline, ""):
        line = line.rstrip()

        if not line:
            continue

        logs[name].append(line)

        if len(logs[name]) > 500:
            logs[name] = logs[name][-500:]

        print(f"[{name}] {line}")

        try:
            asyncio.run(
                emit(
                    name,
                    "console output",
                    [line]
                )
            )
        except Exception:
            pass


def start_server(name, cwd, cmd):
    if name in processes and processes[name].poll() is None:
        return {"status": "already_running"}

    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        shell=True,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        bufsize=1,
    )

    processes[name] = proc

    threading.Thread(
        target=_reader,
        args=(name, proc),
        daemon=True,
    ).start()

    try:
        asyncio.run(
            emit(
                name,
                "status",
                ["running"],
            )
        )
    except Exception:
        pass

    return {
        "status": "started",
        "pid": proc.pid,
    }


def stop_server(name):
    if name not in processes:
        return {"status": "not_found"}

    proc = processes[name]

    if proc.poll() is None:
        proc.terminate()

    try:
        asyncio.run(
            emit(
                name,
                "status",
                ["offline"],
            )
        )
    except Exception:
        pass

    return {"status": "stopped"}


def status():
    out = []

    for name, proc in processes.items():
        running = proc.poll() is None

        cpu = 0
        ram = 0

        if running:
            try:
                p = psutil.Process(proc.pid)
                cpu = p.cpu_percent()
                ram = p.memory_info().rss // 1024 // 1024
            except Exception:
                pass

        out.append(
            {
                "name": name,
                "pid": proc.pid,
                "running": running,
                "cpu": cpu,
                "ram": ram,
            }
        )

    return out


def get_logs(name):
    return logs.get(name, [])


def send_command(name: str, command: str):
    proc = processes.get(name)

    if proc is None:
        return {"error": "not running"}

    try:
        proc.stdin.write(command + "\n")
        proc.stdin.flush()

        try:
            asyncio.run(
                emit(
                    name,
                    "console command",
                    [command],
                )
            )
        except Exception:
            pass

        return {
            "status": "sent",
            "command": command,
        }

    except Exception as e:
        return {
            "error": str(e),
        }
