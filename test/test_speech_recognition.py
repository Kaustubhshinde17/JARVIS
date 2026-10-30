
import sounddevice as sd
from faster_whisper import WhisperModel

DEVICE_ID = 1
SAMPLE_RATE = 16000
DURATION = 5

print("Loading JARVIS speech recognition model...")

model = WhisperModel(
    "tiny",
    device="cpu",
    compute_type="int8"
)

print("JARVIS is ready. Speak now!")

audio = sd.rec(
    int(DURATION * SAMPLE_RATE),
    samplerate=SAMPLE_RATE,
    channels=1,
    dtype="float32",
    device=DEVICE_ID
)

sd.wait()

print("Processing your speech...")

segments, info = model.transcribe(
    audio.flatten(),
    language="en",
    vad_filter=True
)

recognized_text = " ".join(
    segment.text.strip() for segment in segments
)

print("You said:", recognized_text or "No speech recognized.")
