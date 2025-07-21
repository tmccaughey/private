from flask import Flask, send_from_directory, jsonify
from flask_cors import CORS
import json
import os

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/')
def serve_root():
    try:
        # Read and serve the JSON file with proper content type
        json_path = os.path.join(os.path.dirname(__file__), 'file', 'sorted-openapi.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        response = jsonify(data)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Cache-Control'] = 'no-cache'
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/file/sorted-openapi.json')
def serve_openapi():
    try:
        # Read and serve the JSON file with proper content type
        json_path = os.path.join(os.path.dirname(__file__), 'file', 'sorted-openapi.json')
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        response = jsonify(data)
        response.headers['Content-Type'] = 'application/json'
        response.headers['Access-Control-Allow-Origin'] = '*'
        response.headers['Access-Control-Allow-Methods'] = 'GET, OPTIONS'
        response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
        response.headers['Cache-Control'] = 'no-cache'
        return response
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)