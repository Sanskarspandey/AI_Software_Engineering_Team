from agents.base import BaseAgent

from schemas.frontend_project import FrontendProject
from agents.frontend_engineer.prompt import SYSTEM_PROMPT

from tools.project_generator import ProjectGenerator


class FrontendEngineerAgent(BaseAgent):

    def __init__(self):

        super().__init__("Frontend Engineer")

        self.structured_llm = self.llm.with_structured_output(
            FrontendProject
        )

    def invoke(self, state):

        self.log_start()

        srs = state["srs"]
        ui = state["ui_design"]
        backend = state["backend_project"]

        prompt = f"""
Project Name:
{srs.project_name}

Executive Summary:
{srs.executive_summary}

Backend Description:
{backend.description}

Generate a complete React frontend.

Return a FrontendProject object.
"""

        frontend = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", prompt),
            ]
        )

        state["frontend_project"] = frontend

        generator = ProjectGenerator(
            "generated_projects/airbnb_clone"
        )

        generator.write_generated_files(
            frontend.files
        )

        state["next_agent"] = "QA Engineer"

        self.log_end()

        return state


frontend_engineer = FrontendEngineerAgent()