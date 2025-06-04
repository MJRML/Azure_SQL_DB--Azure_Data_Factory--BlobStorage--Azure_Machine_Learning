#Create an Inference Script(socre.py)

#This file defines how input data will be scored by the model

#import packages required
import os # to interact with the enviroment - get model dir
import joblib # for laoding the trained model
import json # used to parse the trained model
import numpy as np
import pandas as pd

def init(): #runs when the web service starts
    model_path = os.path.join(os.getenv("AZUREML_MODEL_DIR"), "LR_model.pkl") #loads serialized model we created in the steps before LR.model.pkl
    global model
    model = joblib.load(model_path) #stores global variable to reuse it in every prediction

def run(raw_data): #Called every time a request is sent to the deployed model API. - Accepts input data as a JSON-formatted string
    try:
        data = json.loads(raw_data) # Converts raw JSON string to a Python dict or list.

        # Handle different input shapes
        if isinstance(data, dict) and "data" in data:
            inputs = data["data"]
        else:
            inputs = data

        # Ensure input is always a list of dictionaries
        if isinstance(inputs, dict):
            inputs = [inputs]

        input_df = pd.DataFrame(inputs) # Converts input JSON into a pandas DataFrame to match the format used when the model was trained.

        # Predict
        prediction = model.predict(input_df) #Calls the model’s .predict() method on the input data.
        return {"result": prediction.tolist()} #Converts the prediction result (NumPy array) to a list and wraps it in a dictionary for JSON output.

    except Exception as e:
        return {"error": str(e)}


