# agents/incident_agent.py

from knowledge.retrieval import (
    retrieve_incidents
)

from agents.llm import llm


def incident_agent(state):
    print("INCIDENT AGENT EXECUTED")

    docs = retrieve_incidents(
        state["service_name"]
    )

    # Guard Clause
    if not docs:

        state["incident_analysis"] = """
        No similar incidents found in the knowledge base.
        """
        state["incident_data_found"] = False
        state["current_step_index"] += 1

        return state

    context = "\n\n".join(docs)
    state["incident_data_found"] = True

    prompt = f"""
    You are an Incident Analysis Agent.
    Use ONLY the information present in the context.

    If information is unavailable,
    explicitly say so.

    Context:
    {context}

    Service:
    {state['service_name']}

    Identify:

    - similar incidents
    - severity
    - root causes
    - lessons learned

    Return a concise analysis.
    """

    response = llm.invoke(prompt)

    state["incident_analysis"] = (
        response.content
    )
    state["current_step_index"] += 1
    return state