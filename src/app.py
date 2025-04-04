import threading

from pynput import keyboard

# Define your hotkey (e.g. Ctrl + Option + H on macOS)
HOTKEY_COMBO = {keyboard.Key.ctrl_l, keyboard.Key.alt_l, keyboard.KeyCode(char="h")}
current_keys = set()


def on_activate():
    print("✨ Hotkey pressed! Do your thing here.")


def on_press(key):
    current_keys.add(key)
    if all(k in current_keys for k in HOTKEY_COMBO):
        on_activate()


def on_release(key):
    if key in current_keys:
        current_keys.remove(key)


def start_listener():
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


# Run listener in a thread so it doesn't block main thread (useful if you add tray later)
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Keep the main script running (or add tray app here)
print("🔍 Listening for hotkey... Press Ctrl + Option + H to trigger.")
try:
    while True:
        pass  # Or replace with logic to run other tasks
except KeyboardInterrupt:
    print("👋 Exiting...")
