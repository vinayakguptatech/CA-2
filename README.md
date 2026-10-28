# Employee Attrition Prediction ML API

A machine learning project that predicts employee attrition using a trained ML model served through a FastAPI REST API and packaged with Docker.

## Project Overview

Employee attrition refers to employees leaving an organization. This project uses HR analytics data to predict whether an employee may leave based on available employee attributes.

## Tech Stack

- Python
- Pandas and NumPy
- Scikit-learn
- FastAPI
- Uvicorn
- Docker
- Pytest
- GitHub Actions

## Project Structure

```text
empolyee-attrition-ml/
├── .github/
│   └── workflows/
│       └── ci.yml
├── tests/
│   └── test_api.py
├── .dockerignore
├── .gitignore
├── Dockerfile
├── main.py
├── model.joblib
├── requirements.txt
├── sample_input.json
└── WA_Fn-UseC_-HR-Employee-Attrition.csv
```

## Run Locally Using Python

### 1. Clone the repository

```bash
git clone https://github.com/vinayakguptatech/CA-2.git
cd CA-2
```

### 2. Create and activate a virtual environment

**macOS/Linux:**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

**Windows PowerShell:**

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 4. Start the API

```bash
uvicorn main:app --host 0.0.0.0 --port 8000
```

Open the interactive API documentation:

http://localhost:8000/docs

## Run with Docker

Ensure Docker Desktop is installed and running.

### 1. Clone the repository

```bash
git clone https://github.com/vinayakguptatech/CA-2.git
cd CA-2
```

### 2. Build the Docker image

```bash
docker build -t employee-attrition-api .
```

### 3. Run the container

```bash
docker run --rm -p 8000:8000 employee-attrition-api
```

Open http://localhost:8000/docs to explore and test the API.

To stop the container, press `Ctrl + C` in the terminal where it is running.

## API Endpoints

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/` | Home endpoint |
| GET | `/health` | Health check |
| POST | `/predict` | Predict employee attrition |

Use `/docs` to submit a sample JSON request to the prediction endpoint.

The request format is available in `sample_input.json`.

## Run Tests

Install the project dependencies first, then run:

```bash
python -m pytest -v
```

## Model

The trained model is stored in `model.joblib`. The application loads this model to generate predictions using the employee input fields supported by the API.

## Dataset

The project uses the IBM HR Analytics Employee Attrition dataset included in this repository.

## Continuous Integration

GitHub Actions automatically runs the test suite on pushes to the `main` branch and pull requests targeting `main`.

## Author

**Vinayak Gupta**

GitHub: [@vinayakguptatech](https://github.com/vinayakguptatech)

Repository: [Employee Attrition Prediction ML API](https://github.com/vinayakguptatech/CA-2)
    