from pathlib import Path


def write_file(path: str, content: str) -> None:
    """
    Write content to any file path.
    Creates parent directories if they do not exist.
    """

    Path(path).parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as file:
        file.write(content)


def read_file(path: str) -> str:
    """
    Read and return file contents.
    """

    with open(path, "r", encoding="utf-8") as file:
        return file.read()


def write_markdown(filename: str, content: str) -> None:
    """
    Save a markdown document inside the docs folder.
    """

    Path("docs").mkdir(parents=True, exist_ok=True)

    with open(f"docs/{filename}", "w", encoding="utf-8") as file:
        file.write(content)