import asyncio

PROCESSES = {}


async def start(uuid, command, cwd):
    if uuid in PROCESSES:
        return

    proc = await asyncio.create_subprocess_shell(
        command,
        cwd=cwd,
        stdin=asyncio.subprocess.PIPE,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.STDOUT,
    )

    PROCESSES[uuid] = proc


async def stop(uuid):
    proc = PROCESSES.get(uuid)

    if not proc:
        return

    proc.kill()
    await proc.wait()

    del PROCESSES[uuid]


async def send(uuid, command):
    proc = PROCESSES.get(uuid)

    if not proc:
        return False

    proc.stdin.write((command + "\n").encode())
    await proc.stdin.drain()

    return True

def get_process(uuid):
    return PROCESSES.get(uuid)
