from typing import TypedDict
from schemas.product import ProductSpec

class SoftwareProjectState(TypedDict):

    user_request: str

    need_clarification: bool

    clarification_questions: list[str]

    next_agent: str

    reasoning: str

    product_spec: ProductSpec | None

    srs: str

    ui_design: str

    backend_code: str

    frontend_code: str

    database_schema: str

    qa_report: str

    deployment_status: str