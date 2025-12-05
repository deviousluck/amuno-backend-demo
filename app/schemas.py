from typing import List
from pydantic import BaseModel, Field

class PredictionInput(BaseModel):
    """
    Input schema for the prediction endpoint.
    """
    field_id: str = Field(..., description="The ID of the field to predict for")
    sample_values: List[float] = Field(..., description="List of sample values to compute risk from")

class PredictionOutput(BaseModel):
    """
    Output schema for the prediction endpoint.
    """
    field_id: str = Field(..., description="The ID of the field (always 'F1' in this demo)")
    risk_score: float = Field(..., description="Calculated risk score between 0 and 1")
    method: str = Field(..., description="The method used for calculation")
