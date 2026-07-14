from agents.base import BaseAgent

from schemas.product import ProductSpec
from agents.product_manager.prompt import SYSTEM_PROMPT

from utils.markdown import generate_product_markdown
from tools.file_tools import write_markdown


class ProductManagerAgent(BaseAgent):

    def __init__(self):
        super().__init__("Product Manager")

        self.structured_llm = self.llm.with_structured_output(ProductSpec)

    def invoke(self, state):

        self.log_start()

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", state["user_request"])
            ]
        )

        state["product_spec"] = result
        state["next_agent"] = "Business Analyst"

        markdown = generate_product_markdown(result)

        write_markdown(
            "product_spec.md",
            markdown
        )

        self.log_end()

        return state


product_manager = ProductManagerAgent()