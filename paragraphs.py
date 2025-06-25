import random

# Collection of shorter paragraphs for typing practice
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog.",
    
    "Technology shapes our daily lives in amazing ways.",
    
    "Reading books expands knowledge and improves thinking skills.",
    
    "Climate change requires urgent global action today.",
    
    "Cooking combines creativity, science, and tradition beautifully.",
    
    "Regular exercise keeps both body and mind healthy.",
    
    "Music connects people across all language barriers.",
    
    "Education opens doors to endless new opportunities.",
    
    "The internet transformed how we share information.",
    
    "Photography captures precious moments in time forever.",
    
    "Space exploration expands human knowledge boundaries constantly.",
    
    "Good communication builds stronger relationships every day.",
    
    "Conservation protects our planet for future generations.",
    
    "Innovation drives progress throughout human civilization.",
    
    "Travel creates memories and broadens life perspectives."
]

def get_random_paragraph():
    """Return a random paragraph for typing practice"""
    return random.choice(PARAGRAPHS)
