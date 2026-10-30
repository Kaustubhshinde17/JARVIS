
import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 175)
engine.setProperty("volume", 1.0)

print("JARVIS is initializing...")

engine.say("Hello Kaustubh. All systems are online.")
engine.runAndWait()

print("Voice test completed.")
