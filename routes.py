from flask import render_template, jsonify
import os
from openai import OpenAI
from app import app

# Initialize OpenAI client
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

@app.route('/')
def index():
    """Main typing test page"""
    return render_template('index.html')

@app.route('/api/paragraph')
def get_paragraph():
    """API endpoint to get a random paragraph for typing test"""
    try:
        # Generate random paragraph using OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{
                "role": "user", 
                "content": "Generate a random 2-sentence English paragraph for typing practice. Make it interesting and varied in topic. Only return the paragraph text, no extra formatting or quotes."
            }],
            max_tokens=100,
            temperature=0.9
        )
        
        paragraph = response.choices[0].message.content.strip()
        return jsonify({'text': paragraph})
        
    except Exception as e:
        print(f"OpenAI API error: {e}")
        # Fallback paragraph if API fails
        fallback_paragraph = "The quick brown fox jumps over the lazy dog. This is a fallback sentence for typing practice."
        return jsonify({'text': fallback_paragraph})
