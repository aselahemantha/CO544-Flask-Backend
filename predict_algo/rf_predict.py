from flask import Flask, request, jsonify
import pickle
import pandas as pd

model_path = ''
with open(model_path, 'rb') as file:
    model = pickle.load(file)


def predict():
    try:
        data = request.get_json(force=True)
        data_df = pd.DataFrame([data])
        prediction = model.predict(data_df)

        return jsonify({'prediction': prediction.tolist()})

    except Exception as e:
        return jsonify({'error': str(e)})
