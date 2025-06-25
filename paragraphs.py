import random

# Collection of perfectly sized two-line paragraphs for typing practice
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog.\nThis pangram contains every letter perfectly.",
    
    "Technology shapes our modern world every day.\nInnovation never stops moving forward rapidly.",
    
    "Reading books expands knowledge and skills.\nEvery page opens new adventures ahead.",
    
    "Climate change needs urgent action now.\nWe must protect our beautiful planet.",
    
    "Cooking combines art, science, and tradition.\nEvery recipe tells cultural stories.",
    
    "Exercise keeps both body and mind healthy.\nDaily movement boosts energy levels.",
    
    "Music connects people across all barriers.\nRhythms speak to every human soul.",
    
    "Education opens doors to new opportunities.\nLearning builds success foundations.",
    
    "Internet transformed global information sharing.\nNetworks connect minds across continents.",
    
    "Photography captures precious life moments.\nImages preserve memories for generations.",
    
    "Space exploration expands human knowledge.\nWe discover amazing worlds beyond Earth.",
    
    "Communication builds stronger relationships.\nListening creates meaningful connections.",
    
    "Conservation protects our future planet.\nSmall actions make big differences.",
    
    "Innovation drives civilization progress forward.\nCreative thinking solves complex problems.",
    
    "Travel broadens life perspectives greatly.\nNew cultures teach valuable lessons."
]

def get_random_paragraph():
    """Return a random paragraph for typing practice"""
    return random.choice(PARAGRAPHS)
