from agents.registry import AGENT_REGISTRY
from utils.logger import console


def router_node(state):

    next_agent = state["next_agent"]

    agent = AGENT_REGISTRY.get(next_agent)

    if agent is None:
        console.print(f"[red]Unknown agent: {next_agent}[/red]")
        return state

    console.print(f"[yellow]Routing to {next_agent}[/yellow]")

    return agent.invoke(state)