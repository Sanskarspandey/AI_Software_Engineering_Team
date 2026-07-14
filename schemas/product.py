from pydantic import BaseModel, Field


class ProductSpec(BaseModel):

    product_name: str = Field(description="Name of the product")

    vision: str = Field(description="Overall vision")

    problem_statement: str = Field(description="Problem being solved")

    target_users: list[str] = Field(default_factory=list)

    core_features: list[str] = Field(default_factory=list)

    mvp_scope: list[str] = Field(default_factory=list)

    future_scope: list[str] = Field(default_factory=list)

    risks: list[str] = Field(default_factory=list)

    success_metrics: list[str] = Field(default_factory=list)