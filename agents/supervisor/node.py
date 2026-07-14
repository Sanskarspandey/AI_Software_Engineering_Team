from models.llm import llm
from schemas.supervisor import SupervisorDecision
from agents.supervisor.prompt import SYSTEM_PROMPT

structured_llm = llm.with_structured_output(SupervisorDecision)


def supervisor_node(state):

    result = structured_llm.invoke(
        [
            ("system", SYSTEM_PROMPT),
            ("human", state["user_request"])
        ]
    )

    # Validation
    if result.need_clarification and not result.questions:
        result.questions = [
            "Please provide more details about your application requirements."
        ]

    state["need_clarification"] = result.need_clarification
    state["clarification_questions"] = result.questions
    state["next_agent"] = result.next_agent
    state["reasoning"] = result.reasoning

    return state