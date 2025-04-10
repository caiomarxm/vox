import os
import threading

from pynput import keyboard
from pynput.keyboard import Key

from src.core.system.clipboard import paste_content
from src.core.system.recording import audio_recorder
from src.core.transcribe.transcribe import transcribe_audio

# Define your hotkey (e.g. Option + Space on macOS)
RECORDING_HOTKEY = {
    Key.alt_l,
    Key.space,
}

current_keys = set()


#
# Handle Keyboard
#


def on_activate():
    if not audio_recorder.is_recording:
        audio_recorder.start_recording()
    else:
        filename = audio_recorder.stop_recording()

        transcription = transcribe_audio(filename)
        print(f"🔊 Transcription: {transcription}")

        paste_content(transcription)
        print("✅ Copied transcription to clipboard")

        os.remove(filename)
        print(f"🗑️ Deleted recording file: {filename}")


def on_press(key):
    current_keys.add(key)
    if all(k in current_keys for k in RECORDING_HOTKEY):
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
print("🔍 Listening for hotkey... Press Option + Space to trigger.")

try:
    while True:
        pass  # Or replace with logic to run other tasks
except KeyboardInterrupt:
    print("👋 Exiting...")
