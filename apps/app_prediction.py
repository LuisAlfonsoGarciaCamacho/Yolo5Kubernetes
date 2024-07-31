# prediction_app.py
import torch
import io
from PIL import Image
from flask import Flask, request, send_file
from flask_cors import CORS
import logging
import numpy as np

app = Flask(__name__)
CORS(app)

logging.basicConfig(level=logging.DEBUG)

try:
    model = torch.hub.load('ultralytics/yolov5', 'yolov5s')
    logging.info("Modelo cargado exitosamente")
except Exception as e:
    logging.error(f"Error al cargar el modelo: {str(e)}")

@app.route('/predict', methods=['POST'])
def predict():
    try:
        logging.info("Recibida solicitud de predicción")
        if 'file' not in request.files:
            logging.warning("No file part in request")
            return "No file part", 400
        file = request.files['file']
        if file.filename == '':
            logging.warning("No selected file")
            return "No selected file", 400

        logging.info(f"Archivo recibido: {file.filename}")
        img = Image.open(io.BytesIO(file.read()))
        logging.info("Imagen abierta correctamente")
        
        results = model(img)
        logging.info("Predicción realizada")
        
        # Obtener la imagen procesada
        img_processed = results.render()[0]  # Esto devuelve un numpy array
        logging.info("Resultados renderizados")

        # Convertir numpy array a imagen PIL
        img_pil = Image.fromarray(img_processed.astype(np.uint8))

        # Guardar en buffer
        img_bytes = io.BytesIO()
        img_pil.save(img_bytes, format='JPEG')
        img_bytes.seek(0)
        logging.info("Imagen procesada guardada en buffer")

        return send_file(img_bytes, mimetype='image/jpeg')
    except Exception as e:
        logging.error(f"Error durante la predicción: {str(e)}")
        return str(e), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
