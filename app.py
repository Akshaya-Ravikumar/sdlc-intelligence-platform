# app.py

from orchestration.workflow import graph

def run_query(query):

    state = {
        "query": query,
        "service_name": "",
        "change_type": "",
        "intent": "",
        "execution_plan": [],
        "current_step_index": 0,
        "dependency_analysis": "",
        "incident_analysis": "",
        "test_recommendations": "",
        "risk_assessment": "",
        "final_report": "",
        "dependency_data_found": False,
        "incident_data_found": False
    }

    for event in graph.stream(state):

        print("\nNODE EXECUTED:")
        print(event)

    return graph.invoke(state)


if __name__ == "__main__":

    result = run_query(
        "What is the impact of changing Transaction service API?"
    )

    print(result["final_report"])