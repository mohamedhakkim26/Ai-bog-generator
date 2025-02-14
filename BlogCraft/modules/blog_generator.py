import google.generativeai as genai
from config import GOOGLE_GEMINI_API_KEY

genai.configure(api_key=GOOGLE_GEMINI_API_KEY)

def generate_blog(title, keywords, word_count):
    model = genai.GenerativeModel("gemini-1.5-pro")
    prompt = f"""
    Generate an engaging blog post titled '{title}' using the keywords: {keywords}.
    The content should be approximately {word_count} words, structured with an introduction,
    subheadings, citations (if needed), and a conclusion.
    """
    response = model.generate_content(prompt)
    return response.text if response else "Error generating blog content."
