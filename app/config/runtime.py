from app.config.config import load

CONFIG = {}


def reload():
    global CONFIG
    CONFIG = load()
    return CONFIG


reload()
