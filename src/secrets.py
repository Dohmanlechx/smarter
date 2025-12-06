from dotenv import load_dotenv
import os

load_dotenv()

def load_api_key():
    load_dotenv()
    return os.getenv("GEMINI_API_KEY")