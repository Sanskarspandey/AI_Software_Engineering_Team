from pathlib import Path

from schemas.generated_file import GeneratedFile


class ProjectGenerator:

    def __init__(self, project_root: str):
        self.project_root = Path(project_root)

    def create_directory(self, relative_path: str):
        (self.project_root / relative_path).mkdir(
            parents=True,
            exist_ok=True
        )

    def write_file(self, relative_path: str, content: str):
        file_path = self.project_root / relative_path

        file_path.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(file_path, "w", encoding="utf-8") as file:
            file.write(content)

    def write_generated_files(
        self,
        files: list[GeneratedFile]
    ):
        """
        Write every generated file to disk.
        """

        for generated_file in files:
            self.write_file(
                generated_file.path,
                generated_file.content
            )