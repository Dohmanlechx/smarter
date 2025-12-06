from google import genai
from google.genai import types
from .secrets import GEMINI_API_KEY

def ask_ai(data):
    client = genai.Client(api_key=GEMINI_API_KEY)

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Summarize {data}, in both English and Swedish, only the summarization themselves.",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )

    return response.text