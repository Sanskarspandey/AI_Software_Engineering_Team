from agents.product_manager.node import product_manager
from agents.business_analyst.node import business_analyst
from agents.ui_designer.node import ui_designer
from agents.database_engineer.node import database_engineer
from agents.backend_engineer.node import backend_engineer


AGENT_REGISTRY = {
    "Product Manager": product_manager,
    "Business Analyst": business_analyst,
    "UI Designer": ui_designer,
    "Database Engineer": database_engineer,
    "Backend Engineer": backend_engineer,
}