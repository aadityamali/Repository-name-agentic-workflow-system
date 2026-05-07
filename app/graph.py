from langgraph.graph import StateGraph, END

from app.state import AgentState

from app.agents.router import router
from app.agents.planner import planner
from app.agents.retriever import retriever
from app.agents.generator import generator
from app.agents.evaluator import evaluator

from app.agents.specialized.healthcare import healthcare_agent
from app.agents.specialized.finance import finance_agent
from app.agents.specialized.coding import coding_agent


workflow = StateGraph(AgentState)


# ------------------------
# ADD NODES
# ------------------------

workflow.add_node("router", router)

workflow.add_node("planner", planner)

workflow.add_node("retriever", retriever)

workflow.add_node("generator", generator)

workflow.add_node("evaluator", evaluator)

workflow.add_node("healthcare", healthcare_agent)

workflow.add_node("finance", finance_agent)

workflow.add_node("coding", coding_agent)


# ------------------------
# ENTRY POINT
# ------------------------

workflow.set_entry_point("router")


# ------------------------
# CONDITIONAL ROUTING
# ------------------------

def route_decision(state):

    route = state.get("route")

    if route == "healthcare":
        return "healthcare"

    elif route == "finance":
        return "finance"

    elif route == "coding":
        return "coding"

    return "planner"


workflow.add_conditional_edges(
    "router",
    route_decision,
    {
        "healthcare": "healthcare",
        "finance": "finance",
        "coding": "coding",
        "planner": "planner"
    }
)


# ------------------------
# HEALTHCARE FLOW
# ------------------------

workflow.add_edge("healthcare", "retriever")

workflow.add_edge("retriever", "generator")

workflow.add_edge("generator", "evaluator")

workflow.add_edge("evaluator", END)


# ------------------------
# FINANCE FLOW
# ------------------------

workflow.add_edge("finance", END)


# ------------------------
# CODING FLOW
# ------------------------

workflow.add_edge("coding", END)


# ------------------------
# GENERAL FLOW
# ------------------------

workflow.add_edge("planner", "retriever")


# ------------------------
# COMPILE GRAPH
# ------------------------

graph = workflow.compile()