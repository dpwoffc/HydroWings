import httpx
from app.config import CONFIG

async def heartbeat():
    url = CONFIG["remote"] + "/api/remote/servers"

    headers = {
        "Authorization": "Bearer " + CONFIG["token"],
        "Accept": "application/json",
    }

    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get(url, headers=headers)

    print("STATUS:", r.status_code)
    print(r.text)

