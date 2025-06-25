import random

# Collection of two-sentence paragraphs for typing practice
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog. This pangram contains every letter perfectly.",
    
    "Technology shapes our modern world every day. Innovation never stops moving forward rapidly.",
    
    "Reading books expands knowledge and skills. Every page opens new adventures ahead.",
    
    "Climate change needs urgent action now. We must protect our beautiful planet.",
    
    "Cooking combines art, science, and tradition. Every recipe tells cultural stories.",
    
    "Exercise keeps both body and mind healthy. Daily movement boosts energy levels.",
    
    "Music connects people across all barriers. Rhythms speak to every human soul.",
    
    "Education opens doors to new opportunities. Learning builds success foundations.",
    
    "Internet transformed global information sharing. Networks connect minds across continents.",
    
    "Photography captures precious life moments. Images preserve memories for generations.",
    
    "Space exploration expands human knowledge. We discover amazing worlds beyond Earth.",
    
    "Communication builds stronger relationships. Listening creates meaningful connections.",
    
    "Conservation protects our future planet. Small actions make big differences.",
    
    "Innovation drives civilization progress forward. Creative thinking solves complex problems.",
    
    "Travel broadens life perspectives greatly. New cultures teach valuable lessons.",
    
    "Artificial intelligence transforms daily work. Smart machines help solve complex tasks.",
    
    "Ocean waves crash against rocky shores. Nature displays its endless power.",
    
    "Morning coffee brings energy and focus. Caffeine helps start productive days.",
    
    "Garden flowers bloom in bright colors. Spring brings beauty to every yard.",
    
    "Mountain peaks reach toward cloudy skies. Adventure calls from high places."
]

def get_random_paragraph():
    """Return a random paragraph for typing practice"""
    return random.choice(PARAGRAPHS)
