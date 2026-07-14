from agents.base import BaseAgent
from schemas.srs import SRS
from agents.business_analyst.prompt import SYSTEM_PROMPT
from utils.markdown import generate_srs_markdown
from tools.file_tools import write_markdown


class BusinessAnalystAgent(BaseAgent):

    def __init__(self):
        super().__init__("Business Analyst")
        self.structured_llm = self.llm.with_structured_output(SRS)

    def invoke(self, state):

        self.log_start()

        product_spec = state["product_spec"]

        result = self.structured_llm.invoke(
            [
                ("system", SYSTEM_PROMPT),
                ("human", product_spec.model_dump_json(indent=2))
            ]
        )

        state["srs"] = result

        markdown = generate_srs_markdown(result)

        write_markdown("SRS.md", markdown)

        self.log_end()

        return state


business_analyst = BusinessAnalystAgent()