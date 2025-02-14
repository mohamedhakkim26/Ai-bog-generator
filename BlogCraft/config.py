import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

GOOGLE_GEMINI_API_KEY = os.getenv("GOOGLE_GEMINI_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

if not GOOGLE_GEMINI_API_KEY or not OPENAI_API_KEY:
    raise ValueError("API keys missing! Please check .env file or environment variables.")
