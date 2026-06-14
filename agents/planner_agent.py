from agents.llm import llm
from models.planner_models import PlannerOutput

def planner_agent(state):

    planner_llm = llm.with_structured_output(PlannerOutput)

    prompt = f"""
    You are an SDLC Planning Agent.

    Analyze the user query and extract:

    1. intent
       - IMPACT_ANALYSIS
       - INCIDENT_ANALYSIS
       - RISK_ASSESSMENT

    2. service_name

    3. change_type

    Supported change types:

    - API Change
    - Database Schema Change
    - Business Logic Change
    - Configuration Change
    - UI Change
    - Dependency Upgrade
    - New Feature
    - Bug Fix

    If no change type is mentioned,
    use "General Change".

    Query:
    {state['query']}
    """

    result = planner_llm.invoke(prompt)

    print("\nPLANNER OUTPUT")
    print("--------------------")
    print(result)

    state["intent"] = result.intent
    state["service_name"] = result.service_name
    state["change_type"] = (
        result.change_type
        or "General Change"
    )

    if result.intent == "IMPACT_ANALYSIS":
        state["execution_plan"] = [
            "dependency",
            "incident",
            "test",
            "risk",
            "report"
        ]

    elif result.intent == "RISK_ASSESSMENT":
        state["execution_plan"] = [
            "dependency",
            "incident",
            "risk",
            "report"
        ]

    elif result.intent == "INCIDENT_ANALYSIS":
        state["execution_plan"] = [
            "incident",
            "report"
        ]

    else:
        state["execution_plan"] = ["report"]

    state["current_step_index"] = 0

    return state