
def install_lib():
  from keras.models import Sequential
  from keras.layers import LSTM, Dense
def model_6days():
  model = keras.models.Sequential()
  model.add(LSTM(units=50, activation='relu', input_shape=(6, 7)))
  model.add(Dense(units=6))
  model.compile(optimizer='adam', loss='mean_squared_error')
  model.load_weights("/LSTM_6days") #insert path here
  return model
def runmodel(input_sequences,model):
  p=model.predict(x)
  return p