from pydantic import BaseModel, Field


class GeneratedFile(BaseModel):
    """
    Represents one generated source file.
    """

    path: str = Field(
        description="Relative file path from the project root."
    )

    content: str = Field(
        description="Complete contents of the file."
    )