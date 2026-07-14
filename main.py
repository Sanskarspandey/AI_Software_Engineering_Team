from graphs.workflow import graph

state = {
    "user_request": "Build me an Airbnb clone.",
    "need_clarification": False,
    "clarification_questions": [],
    "next_agent": "",
    "reasoning": "",
    "product_spec": None,
    "srs": "",
    "ui_design": "",
    "backend_code": "",
    "frontend_code": "",
    "database_schema": "",
    "qa_report": "",
    "deployment_status": ""
}

result = graph.invoke(state)
