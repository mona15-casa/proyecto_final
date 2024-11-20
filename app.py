from flask import Flask, request, jsonify
from flask_cors import CORS
import joblib
import numpy as np

# Cargar el modelo y el escalador
model = joblib.load('mlp_model.pkl')
scaler = joblib.load('scaler.pkl')

# Inicializar la aplicación Flask
app = Flask(__name__)
CORS(app)  # Habilitar CORS para todas las rutas

@app.route('/prediccion', methods=['POST'])
def predict():
    try:
        # Obtener los datos del request
        data = request.json
        
        # Verificar que todas las características necesarias estén presentes
        required_features = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 
                             'work_type', 'Residence_type', 'avg_glucose_level', 'bmi', 'smoking_status']
        if not all(feature in data for feature in required_features):
            return jsonify({'error': f'Faltan algunas características necesarias: {required_features}'}), 400

        # Extraer los valores en el orden correcto
        features = [data[feature] for feature in required_features]
        
        # Escalar los datos de entrada
        features_scaled = scaler.transform([features])  # Escalar una lista de una sola muestra
        
        # Realizar la predicción
        prediction = model.predict(features_scaled)[0]
        # probability = model.predict_proba(features_scaled).tolist()[0]
        
        # Devolver la predicción y la probabilidad como JSON
        return jsonify({
            'prediction': int(prediction),
            # 'probability': probability
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
