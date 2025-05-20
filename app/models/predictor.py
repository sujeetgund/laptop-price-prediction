import pickle
import os
import pandas as pd
import numpy as np
# from app.utils.preprocessing import preprocess_input

MODEL_PATH = os.path.join("research", "model", "laptop_price_predictor.pkl")

with open(MODEL_PATH, 'rb') as file:
    model = pickle.load(file)

def predict_price(data):
    df = pd.DataFrame([data.dict()])
    # processed = preprocess_input(df)
    prediction = model.predict(df)[0]
    prediction = np.exp(prediction)
    return round(prediction, 2)