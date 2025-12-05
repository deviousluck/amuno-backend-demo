# Architecture Overview

This document outlines the architecture of the Minimal FastAPI Backend Demo.

## Layers

### 1. API Layer (`app/main.py`, `app/schemas.py`)
- **Responsibility**: Handles HTTP requests, validation, and serialization.
- **Components**:
    - **FastAPI App**: The entry point.
    - **Pydantic Schemas**: Define the structure of request and response bodies, ensuring type safety and validation.
    - **Endpoints**: Route handlers that delegate logic to the service layer.

### 2. Service Layer (`app/services.py`)
- **Responsibility**: Contains the business logic.
- **Components**:
    - **PredictionService**: Encapsulates the logic for calculating risk scores. It is decoupled from the HTTP transport layer.

### 3. Domain/Model Layer (`app/models.py`)
- **Responsibility**: Represents the core domain entities.
- **Components**:
    - In this minimal demo, the domain models are closely aligned with schemas, but in a larger app, this would contain ORM models or pure domain classes.

## Data Flow

1. **Request**: Client sends POST request to `/api/v1/predict`.
2. **Validation**: FastAPI/Pydantic validates the JSON body against `PredictionInput`.
3. **Processing**: The endpoint calls `PredictionService.calculate_risk(input_data)`.
4. **Logic**: Service computes mean and normalizes the score.
5. **Response**: Service returns data, which is serialized to JSON matching `PredictionOutput`.

## Future Production Extensions

- **Database**: Add SQLAlchemy or Tortoise ORM in `app/models.py` and `app/database.py` to store predictions.
- **External Services**: Add clients for S3 (file storage) or other APIs.
- **Caching**: Implement Redis caching in the Service layer for repeated calculations.
- **Workers**: Offload heavy processing to a task queue (e.g., Celery).
- **Observability**: Add middleware for structured logging and metrics (OpenTelemetry).
