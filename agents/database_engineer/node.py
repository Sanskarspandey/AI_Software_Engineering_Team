from agents.base import BaseAgent

from schemas.database_design import DatabaseDesign
from agents.database_engineer.prompt import SYSTEM_PROMPT

from utils.markdown import generate_database_markdown


class DatabaseEngineerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Database Engineer")

        self.structured_llm = self.llm.with_structured_output(
            DatabaseDesign
        )

    def invoke(self, state):

        self.log_start()

        srs = state["srs"]
        ui = state["ui_design"]

        functional_requirements = "\n".join(
            f"- {item}" for item in srs.functional_requirements
        )

        screens = "\n".join(
            f"- {item}" for item in ui.screens
        )

        components = "\n".join(
            f"- {item}" for item in ui.components
        )

        human_prompt = f"""
Project Name:
{srs.project_name}

Executive Summary:
{srs.executive_summary}

Functional Requirements:
{functional_requirements}

Application Screens:
{screens}

UI Components:
{components}

Design a scalable database architecture for this application.

Return:

- Database Technology
- Collections
- Relationships
- Indexes
- Validation Rules
- Mongoose Models
- API Dependencies
"""

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", human_prompt),
            ]
        )

        state["database_design"] = result

        markdown = generate_database_markdown(result)

        self.save_document(
            "Database_Design.md",
            markdown
        )

        state["next_agent"] = "Backend Engineer"

        self.log_end()

        return state


database_engineer = DatabaseEngineerAgent()