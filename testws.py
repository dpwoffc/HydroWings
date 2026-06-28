import asyncio
import websockets

TOKEN = "81ac0cdd7d5f1cd3e66190c11ba7de29f87ea1ccec8d368cabb23a8f3c378943"

async def main():
    uri = f"ws://127.0.0.1:8081/ws/servers/discord-bot?token={TOKEN}"

    async with websockets.connect(uri) as ws:
        print("CONNECTED")

        while True:
            print(await ws.recv())

asyncio.run(main())
