import subprocess
import psutil

processes = {}

def start_server(name, cwd, cmd):
    if name in processes and processes[name].poll() is None:
        return {"status": "already_running"}

    proc = subprocess.Popen(
        cmd,
        cwd=cwd,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    processes[name] = proc

    return {
        "status": "started",
        "pid": proc.pid
    }

def stop_server(name):
    if name not in processes:
        return {"status": "not_found"}

    proc = processes[name]

    if proc.poll() is None:
        proc.terminate()

    return {"status": "stopped"}

def status():
    data = []

    for name, proc in processes.items():
        running = proc.poll() is None

        cpu = 0
        ram = 0

        if running:
            try:
                p = psutil.Process(proc.pid)
                cpu = p.cpu_percent()
                ram = p.memory_info().rss // 1024 // 1024
            except:
                pass

        data.append({
            "name": name,
            "pid": proc.pid,
            "running": running,
            "cpu": cpu,
            "ram": ram
        })

    return data
