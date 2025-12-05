import statistics
from app.schemas import PredictionInput, PredictionOutput

class PredictionService:
    """
    Service class containing business logic for predictions.
    """
    
    @staticmethod
    def calculate_risk(data: PredictionInput) -> PredictionOutput:
        """
        Computes the risk score based on sample values.
        
        Logic:
        1. Compute mean of sample_values.
        2. Normalize: (mean - 0.2) / 0.6
        3. Clamp result between 0 and 1.
        """
        if not data.sample_values:
            # Handle empty list case if necessary, though Pydantic ensures list exists.
            # Assuming 0.0 for empty list or raising error. 
            # For this demo, we'll assume valid input or handle div by zero if needed.
            mean_val = 0.0
        else:
            mean_val = statistics.mean(data.sample_values)
            
        # Normalize: (mean - 0.2) / 0.6
        normalized_score = (mean_val - 0.2) / 0.6
        
        # Clamp between 0 and 1
        risk_score = max(0.0, min(1.0, normalized_score))
        
        return PredictionOutput(
            field_id="F1", # As per requirement
            risk_score=round(risk_score, 2), # Rounding for cleaner output
            method="rule+demo"
        )
