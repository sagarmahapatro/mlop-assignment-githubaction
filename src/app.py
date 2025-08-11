from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import logging
import os

log_dir = "src/logs"
os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=os.path.join(log_dir, "predictions.log"),
    format="%(asctime)s - %(message)s",
    level=logging.INFO
)

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
    input_dict = data.dict()
    features = np.array(data.features).reshape(1, -1)
    prediction = model.predict(features)
    logging.info(f"Input: {input_dict}, Prediction: {prediction.tolist()}")
    return {"prediction": prediction.tolist()}
