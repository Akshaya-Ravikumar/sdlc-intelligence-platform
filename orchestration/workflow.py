from langgraph.graph import StateGraph
from orchestration.state import AgentState
from orchestration.router import execution_router

from agents.planner_agent import planner_agent
from agents.dependency_agent import dependency_agent
from agents.incident_agent import incident_agent
from agents.test_agent import test_agent
from agents.risk_agent import risk_agent
from agents.report_agent import report_agent

builder = StateGraph(AgentState)

# Defining nodes
builder.add_node("planner", planner_agent)
builder.add_node("dependency", dependency_agent)
builder.add_node("incident", incident_agent)
builder.add_node("test", test_agent)
builder.add_node("risk", risk_agent)
builder.add_node("report", report_agent)

builder.set_entry_point("planner")

#Defining edges
builder.add_conditional_edges("planner", execution_router)
builder.add_conditional_edges("dependency", execution_router)
builder.add_conditional_edges("incident", execution_router)
builder.add_conditional_edges("test", execution_router)
builder.add_conditional_edges("risk", execution_router)
builder.add_conditional_edges("report", execution_router)

graph = builder.compile()