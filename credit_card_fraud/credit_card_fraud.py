import numpy as np
import pandas as pd

import pickle

# Load the model from the pickle file
with open('credit_card_fraud_final.pkl', 'rb') as file:
    loaded_model = pickle.load(file)

for i in range(2):
    # Get input and split by comma, then convert to floats
    input_data = list(map(float, input('enter the amount and another value separated by comma: ').split(',')))
    # Make predictions using the loaded model
    predictions = loaded_model.predict([input_data])
    # Display the predictions
    print(predictions)