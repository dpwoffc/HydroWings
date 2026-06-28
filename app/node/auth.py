import secrets

NODE_SECRET = secrets.token_hex(32)


def get_secret():
    return NODE_SECRET


def verify(secret: str):
    return secret == NODE_SECRET
