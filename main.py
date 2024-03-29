# fastapi_project/main.py

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
# from prediction_functions import model_6days, runmodel
import numpy as np
from keras.models import Sequential
from keras.layers import LSTM, Dense
import keras
app = FastAPI()

class InputData(BaseModel):
    data: list

@app.post("/predict")
def predict(input_data: InputData):
    # Load the LSTM model
    # model = model_6days()



  model = keras.models.Sequential()
  model.add(LSTM(units=50, activation='relu', input_shape=(6, 7)))
  model.add(Dense(units=6))
  model.compile(optimizer='adam', loss='mean_squared_error')
  model.load_weights("LSTM_6days")
    

    # Prepare input data
  input_sequences = np.array(input_data.data).reshape(1, 6, 7)

    # Perform prediction
  try:
        # prediction = runmodel(input_sequences, model)
   p=model.predict(input_sequences)
   return {"prediction": p.tolist()}
  except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))
