from pydantic import BaseModel, Field


class BackendDesign(BaseModel):
    """
    Represents the backend architecture and generated
    Express.js project files.
    """

    project_name: str = Field(
        description="Backend project name."
    )

    folder_structure: list[str] = Field(
        default_factory=list,
        description="Folders to create."
    )

    dependencies: list[str] = Field(
        default_factory=list,
        description="NPM dependencies."
    )

    dev_dependencies: list[str] = Field(
        default_factory=list,
        description="Development dependencies."
    )

    routes: list[str] = Field(
        default_factory=list,
        description="API routes."
    )

    controllers: list[str] = Field(
        default_factory=list,
        description="Controllers."
    )

    middleware: list[str] = Field(
        default_factory=list,
        description="Middleware."
    )

    models: list[str] = Field(
        default_factory=list,
        description="Database models."
    )

    configuration_files: list[str] = Field(
        default_factory=list,
        description="Configuration files."
    )