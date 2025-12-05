from fastapi import FastAPI
from app.schemas import PredictionInput, PredictionOutput
from app.services import PredictionService

app = FastAPI(
    title="Minimal Backend Demo",
    description="A minimal FastAPI backend for risk prediction.",
    version="1.0.0"
)

@app.post("/api/v1/predict", response_model=PredictionOutput)
def predict(input_data: PredictionInput):
    """
    Calculate risk score based on input sample values.
    """
    return PredictionService.calculate_risk(input_data)

@app.get("/")
def health_check():
    """
    Simple health check endpoint.
    """
    return {"status": "ok", "message": "Service is running"}
