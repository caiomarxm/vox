import platform
import threading
import time
import wave

import pyaudio
import pyautogui
import pyperclip
from pynput import keyboard
from pynput.keyboard import Key

from src.core.transcribe.transcribe import transcribe_audio

# Define your hotkey (e.g. Option + Space on macOS)
RECORDING_HOTKEY = {
    Key.alt_l,
    Key.space,
}

current_keys = set()


# Audio settings
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
FILENAME = "recorded_audio.wav"

# Global variables
audio = pyaudio.PyAudio()
stream = None
frames = []
is_recording = False


#
# Handle Audio
#


def start_recording():
    global stream, frames, is_recording
    if is_recording:
        print("⚠️ Already recording!")
        return

    print("🎙️ Recording started...")
    is_recording = True
    frames = []

    # Open audio stream
    stream = audio.open(
        format=FORMAT, channels=CHANNELS, rate=RATE, input=True, frames_per_buffer=CHUNK
    )

    def record():
        while is_recording:
            data = stream.read(CHUNK)
            frames.append(data)

    threading.Thread(target=record, daemon=True).start()


def stop_recording():
    global stream, is_recording
    if not is_recording:
        print("⚠️ Not recording!")
        return

    print("🛑 Recording stopped. Saving file...")
    is_recording = False
    stream.stop_stream()
    stream.close()

    # Save to file
    with wave.open(FILENAME, "wb") as wf:
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(audio.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b"".join(frames))

    print(f"✅ Saved recording to {FILENAME}")


# TODO: Find a better place for this function
def paste_transcription(transcription: str):
    pyperclip.copy(transcription)

    time.sleep(0.1)

    # Simulate paste shortcut depending on OS
    if platform.system() == "Darwin":  # macOS
        print("🍎 macOS detected")
        command_key = "command"
    else:  # Windows/Linux
        print("🪟 Windows/Linux detected")
        command_key = "ctrl"

    pyautogui.keyDown(command_key)
    pyautogui.press("v")
    pyautogui.keyUp(command_key)


#
# Handle Keyboard
#

IS_RECORDING = False


def on_activate():
    global IS_RECORDING
    IS_RECORDING = not IS_RECORDING

    if IS_RECORDING:
        print("🎙️ Recording started...")
        start_recording()
    else:
        print("🛑 Recording stopped.")
        stop_recording()
        transcription = transcribe_audio(FILENAME)
        print(f"🔊 Transcription: {transcription}")
        paste_transcription(transcription)
        print("✅ Copied transcription to clipboard")


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
