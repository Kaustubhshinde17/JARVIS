
import pyttsx3

engine = pyttsx3.init("sapi5")

for index, voice in enumerate(engine.getProperty("voices")):
    print(f"\nVoice {index}")
    print("Name:", voice.name)
    print("ID:", voice.id)
    print("Languages:", voice.languages)

engine.stop()
