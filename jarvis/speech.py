import pyttsx3


class SpeechEngine:
    def speak(self, text):
        print(f"JARVIS: {text}")

        engine = pyttsx3.init("sapi5")
        engine.setProperty("rate", 175)
        engine.setProperty("volume", 1.0)

        engine.say(text)
        engine.runAndWait()
        engine.stop()