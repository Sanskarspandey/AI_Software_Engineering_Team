from agents.base import BaseAgent

from schemas.srs import SRS
from agents.business_analyst.prompt import SYSTEM_PROMPT

from utils.markdown import generate_srs_markdown


class BusinessAnalystAgent(BaseAgent):

    def __init__(self):
        super().__init__("Business Analyst")
        self.structured_llm = self.llm.with_structured_output(SRS)

    def invoke(self, state):

        self.log_start()

        product_spec = state["product_spec"]

        target_users = "\n".join(
            f"- {user}" for user in product_spec.target_users
        )

        core_features = "\n".join(
            f"- {feature}" for feature in product_spec.core_features
        )

        mvp_scope = "\n".join(
            f"- {item}" for item in product_spec.mvp_scope
        )

        human_prompt = f"""
Project Name:
{product_spec.product_name}

Vision:
{product_spec.vision}

Problem Statement:
{product_spec.problem_statement}

Target Users:
{target_users}

Core Features:
{core_features}

MVP Scope:
{mvp_scope}

Generate a complete Software Requirements Specification.
"""

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", human_prompt),
            ]
        )

        state["srs"] = result

        markdown = generate_srs_markdown(result)

        self.save_document(
            "SRS.md",
            markdown
        )

        state["next_agent"] = "UI Designer"

        self.log_end()

        return state


business_analyst = BusinessAnalystAgent()