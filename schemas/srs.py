from pydantic import BaseModel, Field


class SRS(BaseModel):
    project_name: str = Field(description="Project name")

    executive_summary: str = Field(description="Executive summary")

    functional_requirements: list[str] = Field(default_factory=list)

    non_functional_requirements: list[str] = Field(default_factory=list)

    user_stories: list[str] = Field(default_factory=list)

    use_cases: list[str] = Field(default_factory=list)

    assumptions: list[str] = Field(default_factory=list)

    constraints: list[str] = Field(default_factory=list)

    acceptance_criteria: list[str] = Field(default_factory=list)