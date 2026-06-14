from typing import Optional
from pydantic import BaseModel, Field

class PlannerOutput(BaseModel):

    intent: str = Field(
        description="Intent of the request"
    )

    service_name: str = Field(
        description="Target service name"
    )

    change_type: Optional[str] = Field(
        default="General Change",
        description="Type of change"
    )