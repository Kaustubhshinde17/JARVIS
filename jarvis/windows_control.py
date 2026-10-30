
import os
import subprocess
import webbrowser
from urllib.parse import quote_plus


APPLICATIONS = {
    "notepad": "notepad.exe",
    "calculator": "calc.exe",
    "chrome": r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    "vscode": "code",
    "file explorer": "explorer.exe"
}


def open_application(app_name: str) -> str:
    """Open an approved Windows application.

    Args:
        app_name: Application name: notepad, calculator, chrome,
                  vscode, or file explorer.
    """
    app_name = app_name.lower().strip()

    if app_name not in APPLICATIONS:
        return f"Application {app_name} is not in the approved list."

    app_path = APPLICATIONS[app_name]

    try:
        if app_name == "chrome" and not os.path.exists(app_path):
            return "Chrome was not found at the configured path."

        subprocess.Popen([app_path])
        return f"Successfully opened {app_name}."

    except FileNotFoundError:
        return f"Could not find {app_name} on this computer."

    except Exception as error:
        return f"Failed to open {app_name}: {error}"


def search_youtube(query: str) -> str:
    """Search YouTube for a requested topic or tutorial.

    Args:
        query: The topic to search for on YouTube.
    """
    if not query or not query.strip():
        return "Please provide something to search for."

    search_url = (
        "https://www.youtube.com/results?search_query="
        + quote_plus(query.strip())
    )

    try:
        chrome_path = APPLICATIONS["chrome"]

        if os.path.exists(chrome_path):
            subprocess.Popen([chrome_path, search_url])
        else:
            webbrowser.open(search_url)

        return f"Opened YouTube search results for {query}."

    except Exception as error:
        return f"Unable to open YouTube: {error}"
