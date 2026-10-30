
import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

print("Checking available models...", flush=True)

try:
    for model in client.models.list():
        if "generateContent" in (model.supported_actions or []):
            print(model.name, flush=True)

except Exception as e:
    print(type(e).__name__, e)
