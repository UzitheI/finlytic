import json
import joblib
import numpy as np
from azureml.core.model import Model

def init():
    global model
    # Load the model from the Azure model registry
    model_path = Model.get_model_path('finlytic-categorize')
    model = joblib.load(model_path)

def run(data):
    try:
        # Extract data from the incoming request
        input_data = np.array(json.loads(data)['data'])
        
        # Make predictions
        result = model.predict(input_data)
        
        # Return the predictions
        return json.dumps({'result': result.tolist()})
    except Exception as e:
        error = str(e)
        return json.dumps({"error": error})


