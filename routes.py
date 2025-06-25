from flask import render_template, jsonify
import requests
import random
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
        paragraph = data[0] if data else get_fallback_paragraph()
        return jsonify({'text': paragraph})
    except Exception as e:
        print(f"Bacon Ipsum API error: {e}")
        # Return random fallback paragraph
        return jsonify({'text': get_fallback_paragraph()})

def get_fallback_paragraph():
    """Return a random fallback paragraph when API fails"""
    fallback_paragraphs = [
        "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the alphabet.",
        "Technology shapes our modern world every day. Innovation never stops moving forward rapidly.",
        "Reading books expands knowledge and skills. Every page opens new adventures ahead.",
        "Climate change needs urgent action now. We must protect our beautiful planet.",
        "Cooking combines art, science, and tradition. Every recipe tells cultural stories.",
        "Exercise keeps both body and mind healthy. Daily movement boosts energy levels.",
        "Music connects people across all barriers. Rhythms speak to every human soul.",
        "Education opens doors to new opportunities. Learning builds success foundations.",
        "Internet transformed global information sharing. Networks connect minds across continents.",
        "Photography captures precious life moments. Images preserve memories for generations."
    ]
    return random.choice(fallback_paragraphs)
