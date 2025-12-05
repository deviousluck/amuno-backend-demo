# Minimal FastAPI Backend Demo

This is a minimal, production-ready backend demo built with FastAPI. It provides a prediction endpoint that calculates a risk score based on input values.

## Features

- **FastAPI**: High performance, easy to learn, fast to code, ready for production.
- **Pydantic**: Data validation and settings management using Python type hints.
- **Dockerized**: Easy to deploy and run anywhere.
- **Clean Architecture**: Separation of concerns with services, schemas, and models.

## Installation & Running Locally

1. **Clone the repository** (if applicable) or navigate to the project root.

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the server**:
   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://localhost:8000`.
   Interactive docs: `http://localhost:8000/docs`.

## Usage

### Predict Endpoint

**POST** `/api/v1/predict`

**Example Request:**

```bash
curl -X POST "http://localhost:8000/api/v1/predict" \
     -H "Content-Type: application/json" \
     -d '{
           "field_id": "Field_A",
           "sample_values": [0.4, 0.6, 0.3]
         }'
```

**Example Response:**

```json
{
  "field_id": "F1",
  "risk_score": 0.73,
  "method": "rule+demo"
}
```

## Running with Docker

1. **Build the image**:
   ```bash
   docker build -t fastapi-demo .
   ```

2. **Run the container**:
   ```bash
   docker run -p 8000:8000 fastapi-demo
   ```

## Production Extensions

To take this to a full production environment, consider:

- **Database**: Integrate PostgreSQL or MongoDB for persistent storage.
- **Async Workers**: Use Celery or ARQ for background tasks.
- **Caching**: Add Redis for caching expensive computations.
- **Monitoring**: Integrate Prometheus and Grafana for metrics.
- **CI/CD**: Set up GitHub Actions for automated testing and deployment.
