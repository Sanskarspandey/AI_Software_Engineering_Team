from pathlib import Path


class ProjectGenerator:
    """
    Utility class for creating project folders
    and writing generated source code files.
    """

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)

    def create_directory(self, relative_path: str) -> None:
        """
        Create a directory relative to the project root.
        """
        (self.project_root / relative_path).mkdir(
            parents=True,
            exist_ok=True,
        )

    def write_file(self, relative_path: str, content: str) -> None:
        """
        Write a file relative to the project root.
        """
        file_path = self.project_root / relative_path
        file_path.parent.mkdir(parents=True, exist_ok=True)

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)