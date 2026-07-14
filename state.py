from typing import TypedDict, List


class SoftwareProjectState(TypedDict):

    user_request: str

    clarification_questions: List[str]

    clarification_answers: List[str]

    product_spec: str

    srs: str

    ui_design: str

    database_schema: str

    backend_code: str

    frontend_code: str

    qa_report: str

    deployment_status: str

    next_agent: str