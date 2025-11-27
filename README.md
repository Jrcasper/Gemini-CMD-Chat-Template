# Gemini CMD Chat Template

A Python script that simulates a Windows Command Prompt (CMD) interface to chat with Google's Gemini AI model (specifically `gemini-2.0-flash`).

## Features

-   **CMD Simulation**: Looks and feels like a classic command prompt.
-   **Gemini Integration**: Connects to Google's `gemini-2.0-flash` model.
-   **Logging**: Automatically saves all conversations to `log.txt` with timestamps.
-   **Cross-Platform**: Works on Windows (`cls`) and Linux/macOS (`clear`).

## Prerequisites

-   Python 3.9 or higher.
-   A Google Cloud API Key for Gemini.

## Installation

1.  **Clone or download** this repository.
2.  **Install the required Python package**:

    ```bash
    pip install google-generativeai
    ```

## Configuration

1.  Open `gemini_chat_template.py` in a text editor.
2.  Locate the configuration section at the top:

    ```python
    # --- CONFIGURATION ---
    # WARNING! Paste your NEW API KEY here (keep it safe!)
    API_KEY = "YOUR_API_KEY_HERE" 
    ```

3.  Replace `"YOUR_API_KEY_HERE"` with your actual Gemini API Key.

## Usage

Run the script from your terminal:

```bash
python gemini_chat_template.py
```

### Commands

-   **Chat**: Type anything to chat with Gemini.
-   **`clear`**: Clears the screen and repaints the header.
-   **`exit`**: Closes the application.
-   **Ctrl+C**: Force exit.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
