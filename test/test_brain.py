
from jarvis.brain import ask_jarvis
from jarvis.speech import SpeechEngine

print("Starting JARVIS...", flush=True)

speech = SpeechEngine()

print("Sending request to Gemini...", flush=True)

answer = ask_jarvis("Introduce yourself as JARVIS in two sentences.")

print("JARVIS:", answer, flush=True)

print("Speaking response...", flush=True)
speech.speak(answer)

print("Done!", flush=True)
