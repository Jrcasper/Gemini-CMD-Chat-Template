import os
import sys
import datetime
import google.generativeai as genai

# --- CONFIGURATION ---
# WARNING! Paste your NEW API KEY here (keep it safe!)
# You can get one at https://aistudio.google.com/
API_KEY = "YOUR_API_KEY_HERE" 

# Name of the file where the log will be saved
LOG_FILE = "log.txt"

# Configure the Google library
try:
    # Check if the user hasn't changed the key
    if API_KEY == "YOUR_API_KEY_HERE":
        print("Error: You must set your API_KEY in the script configuration.")
        sys.exit(1)

    genai.configure(api_key=API_KEY)
    
    # --- KEY CHANGE ---
    # Using the specific model: 'gemini-2.0-flash'
    model = genai.GenerativeModel('gemini-2.0-flash')
    
    # Start the chat with empty history
    chat = model.start_chat(history=[])
    
except Exception as e:
    print(f"Error configuring Gemini: {e}")
    print("Try running: pip install --upgrade google-generativeai")
    sys.exit(1)

def save_log(user, response):
    """Saves the interaction to a .txt file without overwriting previous content."""
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] USER: {user}\n")
            f.write(f"[{timestamp}] GEMINI: {response}\n")
            f.write("-" * 40 + "\n")
    except Exception as e:
        print(f"[System]: Error writing to log: {e}")

def clear_screen():
    """Visually clears the console."""
    os.system('cls' if os.name == 'nt' else 'clear')
    show_header()

def show_header():
    print("Microsoft Windows [Version 10.0.Simulated]")
    print("(c) Corporation. All rights reserved.")
    print(f"\n-- CONNECTED TO MODEL: gemini-2.0-flash --")
    print("-- (Type 'exit' to quit, 'clear' to clean screen) --\n")

def main():
    clear_screen()

    while True:
        try:
            # Simulate prompt with current path
            prompt_text = f"{os.getcwd()}>"
            user_input = input(prompt_text).strip()

            if not user_input:
                continue

            if user_input.lower() == "exit":
                break

            if user_input.lower() == "clear":
                clear_screen()
                continue

            # Visual loading feedback
            print("...", end="\r") 
            
            try:
                # Send the message
                response = chat.send_message(user_input)
                
                if response.text:
                    print(f"\n{response.text}\n")
                    save_log(user_input, response.text)
                else:
                    print("\n[AI returned no text]\n")

            except Exception as api_error:
                print(f"\nAPI Error: {api_error}\n")
                save_log(user_input, f"Error: {api_error}")

        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
