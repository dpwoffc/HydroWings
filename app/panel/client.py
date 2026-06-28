import requests

from app.node.register import load_node


def pair():

    node = load_node()

    if not node.get("registered"):
        return {
            "error": "node not registered"
        }

    try:
        r = requests.post(
            node["panel"] + "/api/nodes/pair",
            json={
                "id": node["id"],
                "name": node["name"],
                "secret": node["secret"],
                "token": node["token"]
            },
            timeout=10
        )

        return r.json()

    except Exception as e:
        return {
            "error": str(e)
        }
