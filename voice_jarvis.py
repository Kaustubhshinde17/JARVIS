
import queue
import numpy as np
import sounddevice as sd
from faster_whisper import WhisperModel

from jarvis.speech import SpeechEngine
from jarvis.commands import handle_command
from jarvis.brain import ask_jarvis


SAMPLE_RATE = 16000
MICROPHONE_ID = 1
BLOCK_SIZE = 1024
MAX_SPEECH_SECONDS = 12
SILENCE_SECONDS = 1.0


def listen_for_speech():
    audio_queue = queue.Queue()

    def callback(indata, frames, time_info, status):
        audio_queue.put(indata.copy())

    with sd.InputStream(
        samplerate=SAMPLE_RATE,
        channels=1,
        dtype="float32",
        device=MICROPHONE_ID,
        blocksize=BLOCK_SIZE,
        callback=callback
    ):
        print("Calibrating microphone...")
        ambient = []

        for _ in range(int(SAMPLE_RATE / BLOCK_SIZE * 0.7)):
            chunk = audio_queue.get()
            ambient.append(float(np.sqrt(np.mean(chunk ** 2))))

        threshold = max(0.008, np.mean(ambient) * 3.0)
        print("Listening... speak naturally.")

        frames = []
        started = False
        silent_blocks = 0

        max_blocks = int(
            MAX_SPEECH_SECONDS * SAMPLE_RATE / BLOCK_SIZE
        )

        silence_blocks = max(
            1, int(SILENCE_SECONDS * SAMPLE_RATE / BLOCK_SIZE)
        )

        for _ in range(max_blocks):
            chunk = audio_queue.get()
            level = float(np.sqrt(np.mean(chunk ** 2)))

            if level > threshold:
                started = True
                silent_blocks = 0
                frames.append(chunk)

            elif started:
                frames.append(chunk)
                silent_blocks += 1

                if silent_blocks >= silence_blocks:
                    break

        if not frames:
            return None

        return np.concatenate(frames, axis=0).flatten()


def main():
    speech = SpeechEngine()

    speech.speak("Initializing JARVIS.")

    print("Loading speech recognition model...")

    model = WhisperModel(
        "tiny",
        device="cpu",
        compute_type="int8"
    )

    speech.speak("JARVIS is online. I am listening.")

    while True:
        try:
            audio = listen_for_speech()

            if audio is None:
                continue

            print("Processing speech...")

            segments, _ = model.transcribe(
                audio,
                language="en",
                beam_size=3,
                vad_filter=True
            )

            command = " ".join(
                segment.text.strip()
                for segment in segments
            ).strip()

            command = command.rstrip(".!?").strip()

            if not command:
                print("I didn't catch that.")
                continue

            print(f"You: {command}")

            # Exit command
            if command.lower() in {
                "exit", "quit", "stop jarvis"
            }:
                speech.speak("Goodbye. JARVIS shutting down.")
                break

            # First check existing predefined commands
            response = handle_command(command)

            # If command is unknown, ask Gemini
            if response == "I don't know that command yet.":
                print("Asking Gemini...")
                response = ask_jarvis(command)

            # Speak the final response
            print(f"JARVIS: {response}")
            speech.speak(response)

        except KeyboardInterrupt:
            print("\nJARVIS stopped.")
            break

        except Exception as error:
            print(f"An error occurred: {error}")


if __name__ == "__main__":
    main()
