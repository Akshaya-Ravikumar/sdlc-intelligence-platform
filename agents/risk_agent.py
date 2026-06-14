from agents.llm import llm


def risk_agent(state):

    print("\nRISK AGENT EXECUTED")

    dependency_found = state.get(
        "dependency_data_found",
        False
    )

    incident_found = state.get(
        "incident_data_found",
        False
    )

    if (
        not dependency_found
        and
        not incident_found
    ):

        state["risk_assessment"] = """
Risk Assessment

Risk Score: Unknown

Risk Level: Unknown

Reason:
Insufficient dependency and incident history available.

Recommendation:
Perform architecture review, code review,
and baseline testing before deployment.
"""

        state["current_step_index"] += 1

        return state

    prompt = f"""
    You are a Risk Assessment Agent.

    Service:
    {state['service_name']}

    Change Type:
    {state['change_type']}

    Dependency Analysis:
    {state['dependency_analysis']}

    Incident Analysis:
    {state['incident_analysis']}

    Test Recommendations:
    {state['test_recommendations']}

    Assess:

    1. Risk Score (0-100)

    2. Risk Level
       LOW
       MEDIUM
       HIGH

    3. Deployment Recommendation

    4. Reasoning

    Return professional assessment.
    """

    response = llm.invoke(prompt)

    state["risk_assessment"] = (
        response.content
    )

    state["current_step_index"] += 1

    return state