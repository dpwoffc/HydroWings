from fastapi import APIRouter
from pydantic import BaseModel

from .config import load_node
from .config import save_node

router = APIRouter()


class Register(BaseModel):
    id: int
    name: str
    panel: str
    token_id: str
    token: str


@router.post("/node/register")
def register(req: Register):

    cfg = load_node()

    cfg["id"] = req.id
    cfg["name"] = req.name
    cfg["panel"] = req.panel
    cfg["token_id"] = req.token_id
    cfg["token"] = req.token
    cfg["registered"] = True

    save_node(cfg)

    return {
        "status": "registered",
        "node": cfg
    }


@router.get("/node")
def info():
    return load_node()
