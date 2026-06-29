from pathlib import Path
from fastapi import APIRouter

router = APIRouter()

ROOT = Path("app/runtime/servers")


@router.get("/api/servers/{uuid}/files/list")
async def list_files(uuid: str, directory: str = "/"):
    base = (ROOT / uuid).resolve()
    target = (base / directory.lstrip("/")).resolve()

    if not target.exists():
        return []

    files = []

    for f in sorted(target.iterdir()):
        stat = f.stat()

        files.append({
            "name": f.name,
            "mode": "755" if f.is_dir() else "644",
            "mode_bits": "0755" if f.is_dir() else "0644",
            "size": stat.st_size,
            "is_file": f.is_file(),
            "is_symlink": f.is_symlink(),
            "mime": "inode/directory" if f.is_dir() else "text/plain",
            "created_at": stat.st_ctime,
            "modified_at": stat.st_mtime,
        })

    return files
