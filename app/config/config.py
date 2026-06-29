from pathlib import Path
import json

CONFIG_FILE = Path("config.json")


def load():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {}


def save(data: dict):
    CONFIG_FILE.write_text(
        json.dumps(data, indent=4)
    )


def get(key, default=None):
    return load().get(key, default)
