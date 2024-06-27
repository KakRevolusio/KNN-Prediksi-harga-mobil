from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import pandas as pd

app = FastAPI()

# Load the pre-trained model and preprocessor
model_path = "knn_model.pkl"
preprocessor_path = "preprocessor.pkl"
knn_model = pickle.load(open(model_path, "rb"))
preprocessor = pickle.load(open(preprocessor_path, "rb"))

class CarFeatures(BaseModel):
    model: str
    tahun: int
    transmisi: str
    jarak_tempuh: int
    bahan_bakar: str
    pajak: int
    mpg: int
    ukuran_mesin: float

@app.post("/predict")
def predict_price(features: CarFeatures):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([features.dict()])
    # Preprocess the input data
    input_preprocessed = preprocessor.transform(input_df)
    # Predict the price
    predicted_price = knn_model.predict(input_preprocessed)[0]
    return {"predicted_price": f"Rp {predicted_price:,.0f}"}
