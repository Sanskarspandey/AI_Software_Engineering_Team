from graphs.workflow import graph


def main():

    state = {

        # User Input
        "user_request": "Build me an Airbnb clone.",

        # Supervisor
        "need_clarification": False,
        "clarification_questions": [],
        "reasoning": "",

        # Workflow
        "next_agent": "Product Manager",

        # Generated Artifacts
        "product_spec": None,
        "srs": None,
        "ui_design": None,
        "database_design": None,
        "backend_design": None,
        "frontend_code": "",
        "qa_report": "",
        "deployment_status": ""
    }

    result = graph.invoke(state)

    print("\n========== FINAL STATE ==========\n")

    print("Need Clarification :", result["need_clarification"])
    print()

    print("Questions :")
    for question in result["clarification_questions"]:
        print("-", question)

    print()

    print("Reasoning :")
    print(result["reasoning"])

    print()

    print("Next Agent :", result["next_agent"])


if __name__ == "__main__":
    main()