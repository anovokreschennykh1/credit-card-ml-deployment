from flask import Flask, request, jsonify
import pickle
import random
import numpy as np
import pandas as pd

app = Flask(__name__)

with open('models/model_v1.pkl', 'rb') as f:
    model_v1 = pickle.load(f)
with open('models/model_v2.pkl', 'rb') as f:
    model_v2 = pickle.load(f)

@app.route('/predict', methods=['POST'])
def predict():
    """Эндпоинт для предсказания дефолта."""
    try:
            data = request.get_json()
            df_features = pd.DataFrame(data['features'])
            ab_group = 'v2' if random.random() > 0.5 else 'v1'

            if ab_group == 'v2':
                model = model_v2
            else:
                model = model_v1
            
            prediction = model.predict(df_features)
            probability = model.predict_proba(df_features)[0][1]
    
            return jsonify({
                'prediction': int(prediction[0]),
                'probability': float(probability),
                'model_version': ab_group
            })
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/health', methods=['GET'])
def health():
    """Проверка здоровья сервиса"""
    return jsonify({'status': 'healthy'}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
