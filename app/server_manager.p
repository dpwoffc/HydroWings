import os
import yaml

INSTANCES = "instances"


def slug(text):
    return (
        text.lower()
        .strip()
        .replace(" ", "-")
    )


def list_servers():
    servers = []

    os.makedirs(INSTANCES, exist_ok=True)

    for folder in os.listdir(INSTANCES):
        path = os.path.join(INSTANCES, folder)

        if not os.path.isdir(path):
            continue

        cfg = {
            "name": folder,
            "uuid": folder,   # fallback
            "runtime": "unknown",
            "entry": "",
        }

        daemon = os.path.join(path, "daemon.yml")

        if os.path.exists(daemon):
            with open(daemon) as f:
                cfg.update(yaml.safe_load(f) or {})

        servers.append(cfg)

    return servers


def get_server(value):
    target = slug(value)

    for server in list_servers():

        if slug(server["name"]) == target:
            return server

        if slug(server.get("uuid", "")) == target:
            return server

    return None
