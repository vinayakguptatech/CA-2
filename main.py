import joblib
import pandas as pd

from fastapi import FastAPI, HTTPException, Body

app = FastAPI(
    title="Employee Attrition Prediction API",
    description="Predicts whether an employee may leave.",
    version="1.0.0"
)

model = joblib.load("model.joblib")
FEATURE_COLUMNS = list(model.feature_names_in_)


@app.get("/")
def home():
    return {
        "message": "Employee Attrition Prediction API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy",
        "model_loaded": True
    }


@app.post("/predict")
def predict(data: dict = Body(...)):
    missing = [
        column for column in FEATURE_COLUMNS
        if column not in data
    ]

    if missing:
        raise HTTPException(
            status_code=400,
            detail={"missing_features": missing}
        )

    try:
        input_df = pd.DataFrame([data])
        input_df = input_df[FEATURE_COLUMNS]

        prediction = model.predict(input_df)[0]
        probabilities = model.predict_proba(input_df)[0]

        yes_index = list(model.classes_).index("Yes")
        attrition_probability = float(probabilities[yes_index])

        return {
            "prediction": str(prediction),
            "attrition_probability": round(
                attrition_probability, 4
            )
        }

    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid input: {str(exc)}"
        )