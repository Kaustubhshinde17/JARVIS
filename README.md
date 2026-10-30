# JARVIS – AI-Powered Voice Assistant

JARVIS is a Python-based AI voice assistant inspired by Tony Stark's JARVIS. It combines speech recognition, Google's Gemini AI, text-to-speech, and Windows automation to provide a hands-free desktop assistant.

The goal of this project is to build an intelligent assistant that can understand voice commands, answer questions, and perform tasks on a Windows computer.

## Features

- **Voice Interaction:** Communicate with JARVIS using your microphone.
- **Speech Recognition:** Uses Faster-Whisper to convert spoken commands into text.
- **AI-Powered Conversations:** Integrates Google Gemini to answer general questions and understand natural language.
- **Text-to-Speech:** Uses Python text-to-speech capabilities to respond verbally.
- **Windows Automation:** Open supported desktop applications through voice commands.
- **YouTube Search:** Search YouTube using natural language requests.
- **Function Calling:** Allows Gemini to invoke supported tools to perform actions.

## Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Google Gemini API | AI-powered responses |
| Faster-Whisper | Speech recognition |
| SoundDevice | Microphone input |
| NumPy | Audio processing |
| pyttsx3 | Text-to-speech |
| Edge TTS | Neural voice experimentation |
| python-dotenv | Environment variable management |

## Project Structure

```text
JARVIS/
│
├── jarvis/
│   ├── __init__.py
│   ├── brain.py
│   ├── commands.py
│   ├── speech.py
│   └── windows_control.py
│
├── test/
│   ├── list_models.py
│   ├── test_brain.py
│   ├── test_jarvis_speech.py
│   ├── test_microphone.py
│   ├── test_multiple_speech.py
│   ├── test_speech_recognition.py
│   └── test_voice.py
│
├── .env
├── .gitignore
├── list_voices.py
├── main.py
├── requirements.txt
└── voice_jarvis.py
```

## Getting Started

### Prerequisites

- Python installed on your Windows computer
- A working microphone
- Internet connection
- Google Gemini API key

### 1. Clone the repository

```bash
git clone https://github.com/Kaustubhshinde17/JARVIS.git
```

### 2. Navigate to the project directory

```bash
cd JARVIS
```

### 3. Create a virtual environment

```bash
python -m venv .venv
```

### 4. Activate the virtual environment

For Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Configure environment variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
GEMINI_MODEL=gemini-3.5-flash-lite
```

Replace the placeholder with your own Gemini API key.

**Important:** Never upload your `.env` file or expose API credentials publicly.

### 7. Run JARVIS

```bash
python main.py
```

JARVIS will initialize the microphone, load the speech recognition model, and start listening for voice commands.

## Example Commands

You can interact with JARVIS using natural language.

- "Open Notepad."
- "Open Calculator."
- "Open Chrome."
- "Search YouTube for Spring Boot tutorials."
- "What is artificial intelligence?"
- "Explain how Java HashMap works."

Say "exit", "quit", or "stop JARVIS" to shut down the assistant.

## Security

- API credentials are stored in environment variables.
- `.env` is excluded through `.gitignore`.
- The virtual environment is not committed to the repository.

## Future Improvements

- More natural and expressive neural voices.
- Improved conversational memory.
- More Windows automation capabilities.
- Better wake-word detection.
- Improved speech recognition in noisy environments.
- GUI dashboard for assistant interaction.

## Author

**Kaustubh Shinde**

GitHub: [@Kaustubhshinde17](https://github.com/Kaustubhshinde17)

---

*JARVIS is an ongoing personal project focused on exploring AI, speech processing, and desktop automation using Python.*
