from agents.base import BaseAgent

from schemas.product import ProductSpec
from agents.product_manager.prompt import SYSTEM_PROMPT

from utils.markdown import generate_product_markdown


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

        markdown = generate_product_markdown(result)

        self.save_document(
            "product_spec.md",
            markdown
        )
        state["next_agent"] = "Business Analyst"

        self.log_end()

        return state


product_manager = ProductManagerAgent()
