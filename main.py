from flask import Flask, request, jsonify
import pandas as pd
import joblib
import sklearn

app = Flask(__name__)

try:
    model = joblib.load('model.pkl')
except FileNotFoundError:
    raise FileNotFoundError("Model file 'model.pkl' not found. Please ensure it is in the correct directory.")


@app.route('/predict', methods=['POST'])
def predict_endpoint():
    try:
        data = request.get_json()
        if not data:
            return jsonify({"error": "Brak danych"}), 400

        input_data = pd.DataFrame([data])
        result = model.predict(input_data)

        return jsonify({"prediction": result[0]})
    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
