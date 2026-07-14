from langgraph.graph import StateGraph
from langgraph.graph import START, END

from agents.clarification.node import clarification_node
from state import SoftwareProjectState

from agents.supervisor.node import supervisor_node
from agents.router import router_node


builder = StateGraph(SoftwareProjectState)

builder.add_node(
    "Supervisor",
    supervisor_node
)

builder.add_node(
    "Clarification",
    clarification_node
)

builder.add_node(
    "Router",
    router_node
)

builder.add_edge(
    START,
    "Supervisor"
)

from config import DEVELOPMENT_MODE


def route_after_supervisor(state):

    if state["need_clarification"] and not DEVELOPMENT_MODE:
        return "clarification"

    return "router"


builder.add_conditional_edges(
    "Supervisor",
    route_after_supervisor,
    {
        "clarification": "Clarification",
        "router": "Router",
    },
)
builder.add_edge(
    "Clarification",
    END
)

builder.add_edge(
    "Router",
    END
)


graph = builder.compile()