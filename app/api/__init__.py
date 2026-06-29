from fastapi import APIRouter

from .server import router as server_router
from .server_create import router as create_router
from .server_sync import router as sync_router
from .server_delete import router as delete_router
from .server_power import router as power_router
from .server_resources import router as resources_router
from .server_console import router as console_router
from .server_ws import router as ws_router
from .server_resources import router as resources_router
from .server_files import router as files_router
from .server_file_contents import router as contents_router
from .server_file_write import router as write_router
from .server_create_folder import router as create_folder_router
from .server_create_file import router as create_file_router
from .server_rename import router as rename_router
from .server_delete_file import router as delete_file_router
from .server_download import router as download_router
from .server_upload import router as upload_router
from .server_archive import router as archive_router
from .server_extract import router as extract_router
from .server_compress import router as compress_router

router = APIRouter()

router.include_router(server_router)
router.include_router(create_router)
router.include_router(sync_router)
router.include_router(delete_router)
router.include_router(power_router)
router.include_router(resources_router)
router.include_router(console_router)
router.include_router(ws_router)
router.include_router(resources_router)
router.include_router(files_router)
router.include_router(contents_router)
router.include_router(write_router)
router.include_router(create_folder_router)
router.include_router(create_file_router)
router.include_router(rename_router)
router.include_router(delete_file_router)
router.include_router(download_router)
router.include_router(upload_router)
router.include_router(archive_router)
router.include_router(extract_router)
router.include_router(compress_router)
