
import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

from jarvis.windows_control import (
    open_application,
    search_youtube
)

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    raise ValueError("GEMINI_API_KEY is missing. Check your .env file.")

client = genai.Client(api_key=api_key)

MODEL = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")

INSTRUCTIONS = """
You are JARVIS, a personal AI assistant inspired by Tony Stark's assistant.

PERSONALITY:
- Speak naturally, politely and intelligently.
- Address the user as Sir naturally.
- Maintain a sophisticated British butler personality.
- Keep responses concise.
- Be witty when appropriate.

TOOL USAGE:
- You can open approved Windows applications using open_application.
- You can search YouTube using search_youtube.
- When the user asks to open an application, use open_application.
- When the user requests a YouTube tutorial, use search_youtube.
- For requests involving multiple actions, use the necessary tools.
- Never claim an action succeeded unless the tool reports success.
- Never invent tools or execute arbitrary shell commands.
- If an application is unavailable, explain that honestly.
"""

def ask_jarvis(message):
    try:
        response = client.models.generate_content(
            model=MODEL,
            contents=f"{INSTRUCTIONS}\n\nUser: {message}",
            config=types.GenerateContentConfig(
                tools=[
                    open_application,
                    search_youtube
                ],
                automatic_function_calling=(
                    types.AutomaticFunctionCallingConfig(
                        maximum_remote_calls=5
                    )
                )
            )
        )

        if not response.text:
            return "I couldn't generate a response. Please try again."

        return response.text.strip()

    except Exception as error:
        print(f"Gemini error: {type(error).__name__}: {error}")
        return "I'm having trouble completing that request, Sir."
