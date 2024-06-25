from flask import Flask, request, jsonify, render_template
import pickle
import pandas as pd


model_path = './models/deploy.pkl'
with open(model_path, 'rb') as file:
    model = pickle.load(file)

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        data = request.get_json(force=True)

        data_df = pd.DataFrame([data])

        prediction = model.predict(data_df)

        prediction_mapping = {
            0.0: 'No Diabetic',
            1.0: 'Pre Diabetic',
            2.0: 'Diabetic'
        }

        mapped_prediction = [prediction_mapping.get(pred, 'unknown') for pred in prediction]

        return jsonify({'Diabetic Prediction': mapped_prediction})

    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888)