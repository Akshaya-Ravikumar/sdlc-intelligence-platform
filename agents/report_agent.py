from agents.llm import llm


def report_agent(state):

    print("\nREPORT AGENT EXECUTED")

    dependency_found = state.get(
        "dependency_data_found",
        False
    )

    incident_found = state.get(
        "incident_data_found",
        False
    )

    # No enterprise knowledge found
    if (
        not dependency_found
        and
        not incident_found
    ):

        state["final_report"] = f"""
CHANGE IMPACT ANALYSIS REPORT

Service:
{state['service_name']}

Change Type:
{state['change_type']}

Summary:
No architecture or incident data exists in the
knowledge repository for this service.

Dependency Analysis:
{state['dependency_analysis']}

Incident Analysis:
{state['incident_analysis']}

Recommended Testing:
{state['test_recommendations']}

Risk Assessment:
{state['risk_assessment']}

Conclusion:
Insufficient enterprise knowledge available.
Please onboard architecture documentation,
service catalog information,
and historical incidents into the platform.
"""

        state["current_step_index"] += 1

        return state

    prompt = f"""
    Generate a professional
    Change Impact Analysis Report.

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

    Risk Assessment:
    {state['risk_assessment']}

    Include:

    1. Executive Summary

    2. Impact Analysis

    3. Incident Insights

    4. Testing Recommendations

    5. Risk Assessment

    6. Deployment Strategy
    """

    response = llm.invoke(prompt)

    state["final_report"] = (
        response.content
    )

    state["current_step_index"] += 1

    return state