from pathlib import Path
import yaml

NODE = Path("config/node.yml")


def load_node():
    if not NODE.exists():
        return {}

    with open(NODE) as f:
        return yaml.safe_load(f) or {}


def save_node(data):
    with open(NODE, "w") as f:
        yaml.safe_dump(data, f)
