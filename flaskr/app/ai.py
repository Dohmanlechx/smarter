from google import genai
from google.genai import types
from secrets import load_api_key

def ask_ai(data):
    client = genai.Client(api_key=load_api_key())

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=f"Summarize {data}, in both English and Swedish",
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)
        )
    )

    return response.text