def route_to_agent(state):

    next_agent = state["next_agent"]

    if not next_agent:
        return "end"

    mapping = {
        "Product Manager": "product_manager",
        "Business Analyst": "business_analyst",
        "UI Designer": "ui_designer",
        "Database Engineer": "database_engineer",
        "Backend Engineer": "backend_engineer",
        "Frontend Engineer": "frontend_engineer",
        "QA Engineer": "qa_engineer",
        "DevOps Engineer": "devops_engineer",
    }

    return mapping.get(next_agent, "end")