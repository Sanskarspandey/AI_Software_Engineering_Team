from typing import TypedDict

from schemas.product import ProductSpec
from schemas.srs import SRS
from schemas.ui_design import UIDesign
from schemas.database_design import DatabaseDesign


class SoftwareProjectState(TypedDict):
    """
    Shared state passed between all agents.
    """

    # User Input
    user_request: str

    # Supervisor
    need_clarification: bool
    clarification_questions: list[str]
    reasoning: str

    # Workflow
    next_agent: str

    # Generated Artifacts
    product_spec: ProductSpec | None

    srs: SRS | None

    ui_design: UIDesign | None

    database_design: DatabaseDesign | None
    
    backend_code: str

    frontend_code: str

    qa_report: str

    deployment_status: str