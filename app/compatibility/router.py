from fastapi import APIRouter

from .system import router as system_router
from .servers import router as servers_router
from .update import router as update_router

router = APIRouter()

router.include_router(system_router)
router.include_router(servers_router)
router.include_router(update_router)
