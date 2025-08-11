from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np

# Load trained model
model = joblib.load("models/best_model.pkl")

app = FastAPI(title="California Housing Prediction API")

class HousingInput(BaseModel):
    features: list

@app.get("/")
def root():
    return {"message": "California Housing Prediction API is running"}

@app.post("/predict")
def predict(data: HousingInput):
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    return {"prediction": prediction.tolist()}
