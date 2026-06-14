from typing import TypedDict, List

class AgentState(TypedDict):
    query: str
    service_name: str
    change_type: str
    intent: str
    execution_plan: List[str]
    current_step_index: int
    dependency_analysis: str
    incident_analysis: str
    test_recommendations: str
    risk_assessment: str
    final_report: str
    dependency_data_found: bool
    incident_data_found: bool