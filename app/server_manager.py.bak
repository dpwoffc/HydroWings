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

    if not os.path.exists(INSTANCES):
        os.makedirs(INSTANCES)

    for name in os.listdir(INSTANCES):

        path = os.path.join(INSTANCES, name)

        if not os.path.isdir(path):
            continue

        cfg = {
            "name": name,
            "runtime": "unknown",
            "entry": ""
        }

        daemon = os.path.join(path, "daemon.yml")

        if os.path.exists(daemon):
            with open(daemon, "r") as f:
                data = yaml.safe_load(f) or {}
                cfg.update(data)

        servers.append(cfg)

    return servers

def get_server(name):
    target = slug(name)

    for server in list_servers():
        if slug(server["name"]) == target:
            return server

    return None
