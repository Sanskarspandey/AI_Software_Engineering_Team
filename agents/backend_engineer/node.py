from agents.base import BaseAgent

from schemas.backend_design import BackendDesign
from agents.backend_engineer.prompt import SYSTEM_PROMPT

from tools.project_generator import ProjectGenerator


class BackendEngineerAgent(BaseAgent):

    def __init__(self):

        super().__init__("Backend Engineer")

        self.structured_llm = self.llm.with_structured_output(
            BackendDesign
        )

    def invoke(self, state):

        self.log_start()

        srs = state["srs"]
        ui = state["ui_design"]
        db = state["database_design"]

        functional_requirements = "\n".join(
            f"- {item}" for item in srs.functional_requirements
        )

        screens = "\n".join(
            f"- {item}" for item in ui.screens
        )

        collections = "\n".join(
            f"- {item}" for item in db.collections
        )

        human_prompt = f"""
Project Name:
{srs.project_name}

Functional Requirements:
{functional_requirements}

Screens:
{screens}

Database Collections:
{collections}

Generate the backend architecture.
"""

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", human_prompt)
            ]
        )

        state["backend_design"] = result

        generator = ProjectGenerator(
            "generated_projects/airbnb_clone"
        )

        for folder in result.folder_structure:
            generator.create_directory(folder)

        state["next_agent"] = ""

        self.log_end()

        return state


backend_engineer = BackendEngineerAgent()