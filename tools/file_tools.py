from pathlib import Path


def write_file(path: str, content: str):

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def read_file(path: str):

    with open(path, "r", encoding="utf-8") as f:
        return f.read()