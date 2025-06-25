import random

# Collection of two-line paragraphs for typing practice
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog.\nThis sentence contains all letters of the alphabet.",
    
    "Technology shapes our daily lives in amazing ways.\nFrom smartphones to AI, innovation never stops.",
    
    "Reading books expands knowledge and thinking skills.\nEvery page turns into a new adventure.",
    
    "Climate change requires urgent global action today.\nWe must protect our planet for future generations.",
    
    "Cooking combines creativity, science, and tradition.\nEvery recipe tells a unique cultural story.",
    
    "Regular exercise keeps both body and mind healthy.\nDaily movement boosts energy and improves mood.",
    
    "Music connects people across all language barriers.\nRhythms and melodies speak to every soul.",
    
    "Education opens doors to endless new opportunities.\nLearning builds the foundation for success.",
    
    "The internet transformed how we share information.\nGlobal networks connect minds across the world.",
    
    "Photography captures precious moments in time forever.\nEach image preserves memories for generations.",
    
    "Space exploration expands human knowledge boundaries.\nWe discover new worlds beyond our planet.",
    
    "Good communication builds stronger relationships daily.\nListening and speaking clearly creates connections.",
    
    "Conservation protects our planet for future generations.\nSmall actions today make big differences tomorrow.",
    
    "Innovation drives progress throughout human civilization.\nCreative thinking solves complex global problems.",
    
    "Travel creates memories and broadens life perspectives.\nNew cultures teach us about diversity."
]

def get_random_paragraph():
    """Return a random paragraph for typing practice"""
    return random.choice(PARAGRAPHS)
