import random

# Collection of paragraphs for typing practice
PARAGRAPHS = [
    "The quick brown fox jumps over the lazy dog. This pangram contains every letter of the English alphabet at least once, making it a perfect sentence for typing practice and font testing.",
    
    "Technology has revolutionized the way we communicate, work, and live our daily lives. From smartphones to artificial intelligence, these innovations continue to shape our future in ways we never imagined possible.",
    
    "Reading books expands our knowledge, improves vocabulary, and enhances critical thinking skills. Whether fiction or non-fiction, every book offers a unique journey that enriches our understanding of the world around us.",
    
    "Climate change represents one of the most pressing challenges of our time. Scientists worldwide are working together to develop sustainable solutions that will help preserve our planet for future generations.",
    
    "The art of cooking combines creativity, science, and tradition. Every recipe tells a story, connecting us to different cultures and bringing people together around the dinner table to share memorable experiences.",
    
    "Exercise and physical activity are essential for maintaining good health and well-being. Regular movement strengthens muscles, improves cardiovascular health, and releases endorphins that boost mood and energy levels.",
    
    "Music has the power to transcend language barriers and connect people from different backgrounds. Whether classical, jazz, rock, or electronic, every genre offers unique rhythms and melodies that speak to the human soul.",
    
    "Education opens doors to endless opportunities and empowers individuals to pursue their dreams. Through learning, we develop skills, gain knowledge, and build the foundation for personal and professional success.",
    
    "The internet has transformed how we access information, connect with others, and conduct business. This global network continues to evolve, creating new possibilities for innovation and collaboration across borders.",
    
    "Photography captures moments in time, preserving memories and telling stories through visual imagery. Each photograph reflects the photographer's perspective and invites viewers to see the world through different eyes.",
    
    "Space exploration pushes the boundaries of human knowledge and technological advancement. As we venture beyond Earth, we discover new worlds and gain deeper insights into our place in the vast universe.",
    
    "Effective communication involves both speaking clearly and listening actively. These skills are fundamental to building strong relationships, resolving conflicts, and achieving success in personal and professional endeavors.",
    
    "Environmental conservation requires collective action from individuals, communities, and governments. By making conscious choices about consumption, waste, and energy use, we can protect natural resources for the future.",
    
    "Innovation drives progress and shapes the trajectory of human civilization. From ancient inventions like the wheel to modern breakthroughs in medicine and technology, creative thinking continues to solve complex problems.",
    
    "Travel broadens perspectives and creates lasting memories through exposure to different cultures, landscapes, and ways of life. Each journey offers opportunities for personal growth and deeper understanding of global diversity."
]

def get_random_paragraph():
    """Return a random paragraph for typing practice"""
    return random.choice(PARAGRAPHS)
