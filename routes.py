from flask import render_template, jsonify
from app import app
from paragraphs import get_random_paragraph

@app.route('/')
def index():
    """Main typing test page"""
    return render_template('index.html')

@app.route('/api/paragraph')
def get_paragraph():
    """API endpoint to get a random paragraph for typing test"""
    paragraph = get_random_paragraph()
    return jsonify({'text': paragraph})
