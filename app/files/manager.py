import os

BASE = "instances"

def _root(name):
    return os.path.join(BASE, name)

def list_files(name):
    root = _root(name)

    if not os.path.exists(root):
        return []

    items = []

    for f in os.listdir(root):
        p = os.path.join(root, f)

        items.append({
            "name": f,
            "type": "dir" if os.path.isdir(p) else "file",
            "size": 0 if os.path.isdir(p) else os.path.getsize(p)
        })

    return items

def read_file(name, path):
    full = os.path.join(_root(name), path)

    with open(full, "r", encoding="utf-8") as f:
        return f.read()

def write_file(name, path, content):
    full = os.path.join(_root(name), path)

    os.makedirs(os.path.dirname(full), exist_ok=True)

    with open(full, "w", encoding="utf-8") as f:
        f.write(content)

    return {"status": "saved"}

def mkdir(name, path):
    os.makedirs(os.path.join(_root(name), path), exist_ok=True)
    return {"status":"created"}

def delete(name, path):
    full = os.path.join(_root(name), path)

    if os.path.isdir(full):
        os.rmdir(full)
    elif os.path.exists(full):
        os.remove(full)

    return {"status":"deleted"}
