import json
from pathlib import Path

from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_home():
    response = client.get("/")
    assert response.status_code == 200


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["model_loaded"] is True


def test_prediction():
    project_root = Path(__file__).resolve().parents[1]

    with open(project_root / "sample_input.json") as f:
        sample = json.load(f)

    response = client.post("/predict", json=sample)

    assert response.status_code == 200
    assert response.json()["prediction"] in ["Yes", "No"]
    assert 0 <= response.json()["attrition_probability"] <= 1