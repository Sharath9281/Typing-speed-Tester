from flask import render_template, jsonify
import requests
from app import app

@app.route('/')
def index():
    """Main typing test page"""
    return render_template('index.html')

@app.route('/api/paragraph')
def get_paragraph():
    """API endpoint to get a random paragraph for typing test"""
    try:
        # Fetch random paragraph from Bacon Ipsum API
        response = requests.get('https://baconipsum.com/api/?type=all-meat&paras=1&sentences=2', timeout=10)
        response.raise_for_status()
        data = response.json()
        paragraph = data[0] if data else "The quick brown fox jumps over the lazy dog. This is a fallback sentence for typing practice."
        return jsonify({'text': paragraph})
    except Exception as e:
        # Fallback paragraph if API fails
        fallback_paragraph = "The quick brown fox jumps over the lazy dog. This is a fallback sentence for typing practice."
        return jsonify({'text': fallback_paragraph})
