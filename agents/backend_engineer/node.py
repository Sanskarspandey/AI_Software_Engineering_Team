from agents.base import BaseAgent

from schemas.backend_project import BackendProject
from agents.backend_engineer.prompt import SYSTEM_PROMPT

from tools.project_generator import ProjectGenerator


class BackendEngineerAgent(BaseAgent):

    def __init__(self):

        super().__init__("Backend Engineer")

        self.structured_llm = self.llm.with_structured_output(
            BackendProject
        )

    def invoke(self, state):

        self.log_start()

        srs = state["srs"]
        ui = state["ui_design"]
        database = state["database_design"]

        functional_requirements = "\n".join(
            f"- {item}" for item in srs.functional_requirements
        )

        screens = "\n".join(
            f"- {item}" for item in ui.screens
        )

        collections = "\n".join(
            f"- {item}" for item in database.collections
        )

        relationships = "\n".join(
            f"- {item}" for item in database.relationships
        )

        prompt = f"""
You are generating a complete Express.js backend.

Project Name:
{srs.project_name}

Executive Summary:
{srs.executive_summary}

Functional Requirements:
{functional_requirements}

Screens:
{screens}

Database Collections:
{collections}

Relationships:
{relationships}

Generate a complete production-ready Express.js backend.

Requirements:

- Node.js
- Express.js
- MongoDB
- Mongoose
- JWT Authentication
- MVC Architecture

Generate EVERY required source file.

Return the response as a BackendProject object.
"""

        backend_project = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", prompt)
            ]
        )

        state["backend_project"] = backend_project

        generator = ProjectGenerator(
            "generated_projects/airbnb_clone"
        )

        generator.write_generated_files(
            backend_project.files
        )

        state["next_agent"] = "Frontend Engineer"

        self.log_end()

        return state


backend_engineer = BackendEngineerAgent()