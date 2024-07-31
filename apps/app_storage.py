# storage_app.py
from flask import Flask, request, jsonify, send_from_directory
import os
import logging

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

logging.basicConfig(level=logging.DEBUG)

def get_next_filename(folder):
    existing_files = os.listdir(folder)
    existing_files.sort()
    if existing_files:
        last_file = existing_files[-1]
        last_index = int(last_file.split('.')[0])
        next_index = last_index + 1
    else:
        next_index = 1
    return f"{next_index}.jpg"

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    filename = get_next_filename(UPLOAD_FOLDER)
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    file.save(filepath)
    logging.info(f"File uploaded to {filepath}")
    return jsonify({'message': 'File uploaded successfully', 'filepath': filepath}), 200

@app.route('/uploads/<filename>')
def get_uploaded_image(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)

@app.route('/uploads')
def list_uploaded_images():
    files = os.listdir(UPLOAD_FOLDER)
    return jsonify(files), 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001, debug=True)
