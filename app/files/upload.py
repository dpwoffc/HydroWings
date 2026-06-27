import os
import zipfile
import shutil


def upload_zip(name: str, file):

    upload_dir = "uploads"
    instance_dir = f"instances/{name}"

    os.makedirs(upload_dir, exist_ok=True)
    os.makedirs(instance_dir, exist_ok=True)

    zip_path = os.path.join(upload_dir, f"{name}.zip")

    with open(zip_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    with zipfile.ZipFile(zip_path, "r") as z:
        z.extractall(instance_dir)

    os.remove(zip_path)

    return {
        "status": "uploaded",
        "server": name
    }
