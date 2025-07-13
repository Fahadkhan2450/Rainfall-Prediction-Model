from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):
    pressure: float
    dewpoint: float
    humidity: int
    cloud: int
    sunshine: float
    winddirection: float
    windspeed: float


loaded = pickle.load(open('rainfall_prediction.sav', 'rb'))

# Check if it's a dict and extract model
rainfall_model = loaded["model"] if isinstance(loaded, dict) else loaded

@app.post("/rainfall_prediction")
def rainfall_pred(input_parameters: model_input):
    try:
        # Directly access values from the Pydantic model
        input_list = [
            input_parameters.pressure,
            input_parameters.dewpoint,
            input_parameters.humidity,
            input_parameters.cloud,
            input_parameters.sunshine,
            input_parameters.winddirection,
            input_parameters.windspeed
        ]

        # Prediction
        prediction = rainfall_model.predict([input_list])

        return {
            "prediction": "Rainfall" if prediction[0] == 1 else "No Rainfall"
        }

    except Exception as e:
        return {"error": str(e)}


@app.get("/")
def root():
    return {"message": "Rainfall Prediction API is running. Use POST /rainfall_prediction"}
