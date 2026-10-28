# Employee Attrition Prediction ML API

A machine learning project that predicts employee attrition using an ML model served through a FastAPI REST API and packaged with Docker.

## Project Overview

Employee attrition refers to employees leaving an organization. This project uses HR analytics data to predict whether an employee is likely to leave based on available employee attributes.

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

## Run Locally

### 1. Install dependencies

```bash
pip install -r requirements.txt
```

### 2. Start the API

```bash
uvicorn main:app --reload
```

### 3. Open API documentation

Visit: http://localhost:8000/docs

## Run with Docker

Build the image:

```bash
docker build -t employee-attrition-api .
```

Run the container:

```bash
docker run -d --name employee-attrition-container -p 8000:8000 employee-attrition-api
```

Open http://localhost:8000/docs to explore and test the API.

## Run Tests

```bash
pytest -v
```

## Model

The trained model is stored in `model.joblib`. The application loads this model to generate predictions using the input fields supported by the API.

## Dataset

The project uses the IBM HR Analytics Employee Attrition dataset included in this repository.

## Author

**Vinayak Gupta**

GitHub: [@vinayakguptatech](https://github.com/vinayakguptatech)
