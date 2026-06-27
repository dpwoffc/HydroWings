import yaml

from fastapi import Header, HTTPException

with open("config/auth.yml") as f:
    CONFIG = yaml.safe_load(f)

TOKEN = CONFIG["token"]

def verify_token(authorization: str = Header(None)):

    if authorization is None:
        raise HTTPException(
            status_code=401,
            detail="Missing Authorization Header"
        )

    if authorization != f"Bearer {TOKEN}":
        raise HTTPException(
            status_code=401,
            detail="Invalid Token"
        )
