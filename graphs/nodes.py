from agents.product_manager.node import product_manager
from agents.business_analyst.node import business_analyst


def product_manager_node(state):
    return product_manager.invoke(state)


def business_analyst_node(state):
    return business_analyst.invoke(state)

