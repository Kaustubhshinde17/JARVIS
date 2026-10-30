
import sounddevice as sd

DEVICE_ID = 1
DURATION = 5
SAMPLE_RATE = 16000

print("JARVIS microphone test starting...")
print("Speak normally for 5 seconds!")

try:
    audio = sd.rec(
        int(DURATION * SAMPLE_RATE),
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=DEVICE_ID
    )

    sd.wait()

    print("SUCCESS: Microphone audio captured!")
    print("Audio shape:", audio.shape)
    print("Peak audio level:", float(abs(audio).max()))

except Exception as error:
    print("Microphone error:", error)
