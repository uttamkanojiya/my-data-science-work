import joblib
import pandas as pd
import os

BASE_DIR = os.path.dirname(__file__)
model = joblib.load(os.path.join(BASE_DIR, "model.pkl"))
pipeline = joblib.load(os.path.join(BASE_DIR, "pipeline.pkl"))


def predict_price(data):
    try:
        df = pd.DataFrame([data])
        transformed = pipeline.transform(df)
        prediction = model.predict(transformed)
        return prediction[0]
    except Exception as e:
        raise ValueError(f"Prediction failed: {e}")
