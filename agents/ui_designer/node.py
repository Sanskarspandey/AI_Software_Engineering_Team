from agents.base import BaseAgent

from schemas.ui_design import UIDesign
from agents.ui_designer.prompt import SYSTEM_PROMPT

from utils.markdown import generate_ui_markdown


class UIDesignerAgent(BaseAgent):

    def __init__(self):
        super().__init__("UI Designer")
        self.structured_llm = self.llm.with_structured_output(
            UIDesign
        )

    def invoke(self, state):

        self.log_start()

        srs = state["srs"]

        functional_requirements = "\n".join(
            f"- {item}" for item in srs.functional_requirements
        )

        non_functional_requirements = "\n".join(
            f"- {item}" for item in srs.non_functional_requirements
        )

        user_stories = "\n".join(
            f"- {item}" for item in srs.user_stories
        )

        use_cases = "\n".join(
            f"- {item}" for item in srs.use_cases
        )

        human_prompt = f"""
Project Name:
{srs.project_name}

Executive Summary:
{srs.executive_summary}

Functional Requirements:
{functional_requirements}

Non Functional Requirements:
{non_functional_requirements}

User Stories:
{user_stories}

Use Cases:
{use_cases}

Generate a complete UI Design Specification.
"""

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", human_prompt)
            ]
        )

        state["ui_design"] = result

        markdown = generate_ui_markdown(result)

        self.save_document(
            "UI_Design.md",
            markdown
        )

        state["next_agent"] = "Database Engineer"

        self.log_end()

        return state


ui_designer = UIDesignerAgent()