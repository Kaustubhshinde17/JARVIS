
from datetime import datetime
import subprocess
import webbrowser


def handle_command(command):
    command = command.lower().strip()

    if command in {"hello", "hi", "hey jarvis"}:
        return "Hello! All systems are online."

    elif "time" in command:
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."

    elif "date" in command:
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    elif "open notepad" in command:
        subprocess.Popen(["notepad.exe"])
        return "Opening Notepad."

    elif "open calculator" in command:
        subprocess.Popen(["calc.exe"])
        return "Opening Calculator."

    elif "open youtube" in command:
        webbrowser.open("https://www.youtube.com")
        return "Opening YouTube."

    elif command in {"exit", "quit"}:
        return "__EXIT__"

    return "I don't know that command yet."
