from pydantic import BaseModel, Field


class SupervisorDecision(BaseModel):

    need_clarification: bool = Field(
        description="Whether additional information is required."
    )

    questions: list[str] = Field(
        default_factory=list,
        description="Clarification questions."
    )

    next_agent: str = Field(
        description="Next agent to execute."
    )

    reasoning: str = Field(
        description="Why this decision was made."
    )