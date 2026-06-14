from knowledge.retrieval import retrieve_dependencies
from agents.llm import llm


def dependency_agent(state):

    print("\nDEPENDENCY AGENT EXECUTED")

    service_name = state["service_name"]
    docs = retrieve_dependencies(
        service_name
    )

    # -----------------------------
    # Guard Clause
    # -----------------------------
    if not docs:

        print(
            "No dependency documents found"
        )

        state["dependency_analysis"] = """
        No dependency information found in the knowledge base.
        """
        state["dependency_data_found"] = False
        state["current_step_index"] += 1

        return state

    # -----------------------------
    # Build Context
    # -----------------------------
    
    context = "\n\n".join(docs)

    print(
        f"Retrieved {len(docs)} dependency documents"
    )
    state["dependency_data_found"] = True

    prompt = f"""
    You are a Dependency Analysis Agent.

    Use ONLY the information present in the context.

    If information is unavailable,
    explicitly say so.

    Context:
    {context}

    Service:
    {service_name}

    Identify:

    1. Affected Services
    2. Dependent Applications
    3. Impacted APIs
    4. Owning Teams

    Return a concise analysis.
    """

    response = llm.invoke(prompt)

    state["dependency_analysis"] = (
        response.content
    )

    state["current_step_index"] += 1

    return state