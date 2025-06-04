#Create an Inference Script(socre.py)

#This file defines how input data will be scored by the model

import os
import joblib
import json
import numpy as np
import pandas as pd

def init():
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "LR_model.pkl")
    global model
    model = joblib.load(model_path)

def run(raw_data):
    try:
        data = json.loads(raw_data)

        # Handle different input shapes
        if isinstance(data, dict) and "data" in data:
            inputs = data["data"]
        else:
            inputs = data

        # Ensure input is always a list of dictionaries
        if isinstance(inputs, dict):
            inputs = [inputs]

        input_df = pd.DataFrame(inputs)

        # Predict
        prediction = model.predict(input_df)
        return {"result": prediction.tolist()}

    except Exception as e:
        return {"error": str(e)}


