from abc import ABC, abstractmethod
from typing import Any

from models.llm import llm
from utils.logger import console
from tools.file_tools import write_markdown


class BaseAgent(ABC):

    def __init__(self, name: str):
        self.name = name
        self.llm = llm

    def log_start(self):
        console.print(
            f"\n[bold cyan]========== {self.name} ==========[/bold cyan]"
        )

    def log_end(self):
        console.print(
            f"[bold green]{self.name} completed.[/bold green]\n"
        )

    def save_document(
        self,
        filename: str,
        markdown: str,
    ):
        """
        Save a generated markdown document.
        """

        write_markdown(
            filename,
            markdown
        )

        console.print(
            f"[green]Saved docs/{filename}[/green]"
        )

    @abstractmethod
    def invoke(
        self,
        state: dict[str, Any]
    ):
        pass