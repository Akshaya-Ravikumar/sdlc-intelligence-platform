from agents.llm import llm


def test_agent(state):

    print("\nTEST AGENT EXECUTED")

    if (
        not state.get("dependency_data_found", False)
        and
        not state.get("incident_data_found", False)
    ):

        state["test_recommendations"] = """
Recommended Baseline Test Strategy

- Unit Testing
- Integration Testing
- Regression Testing
- Smoke Testing
- Happy Path Testing

Reason:
No historical dependency or incident data available.
"""

        state["current_step_index"] += 1

        return state

    prompt = f"""
    You are a Test Recommendation Agent.

    Change Type:
    {state['change_type']}

    Dependency Analysis:
    {state['dependency_analysis']}

    Incident Analysis:
    {state['incident_analysis']}

    Recommend:

    - Regression Tests
    - Integration Tests
    - Edge Cases
    - Critical Test Scenarios

    Return concise recommendations.
    """

    response = llm.invoke(prompt)

    state["test_recommendations"] = (
        response.content
    )

    state["current_step_index"] += 1

    return state