from rich.console import Console

console = Console()


def clarification_node(state):
    console.print("\n[bold yellow]===== CLARIFICATION REQUIRED =====[/bold yellow]\n")

    for question in state["clarification_questions"]:
        console.print(f"• {question}")

    return state