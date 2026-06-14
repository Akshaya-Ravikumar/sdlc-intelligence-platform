from langgraph.graph import END


def execution_router(state):

    plan = state["execution_plan"]

    idx = state["current_step_index"]

    print(f"\nROUTER INDEX = {idx}")

    if idx >= len(plan):
        return END

    return plan[idx]