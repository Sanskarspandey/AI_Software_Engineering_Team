from agents.registry import AGENT_REGISTRY
from utils.logger import console


def router_node(state):

    while True:

        next_agent = state["next_agent"]

        if not next_agent:
            break

        agent = AGENT_REGISTRY.get(next_agent)

        if agent is None:
            console.print(f"[red]Unknown agent: {next_agent}[/red]")
            break

        console.print(f"[yellow]Routing to {next_agent}[/yellow]")

        state["next_agent"] = ""

        state = agent.invoke(state)

    return state