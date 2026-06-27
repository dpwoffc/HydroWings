def build_command(runtime: str, entry: str):
    runtime = runtime.lower()

    if runtime == "python":
        return f"python3 {entry}"

    if runtime == "node":
        return f"node {entry}"

    if runtime == "bash":
        return f"bash {entry}"

    return None
