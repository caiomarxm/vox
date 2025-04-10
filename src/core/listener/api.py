import os

from pynput import keyboard
from pynput.keyboard import Key

from src.core.system.clipboard import paste_content
from src.core.system.recording import audio_recorder
from src.core.system.tray import tray_icon
from src.core.transcribe.transcribe import transcribe_audio

# TODO: Make this configurable
RECORDING_HOTKEY = {
    Key.ctrl_l,
    Key.space,
}

current_keys = set()


def on_activate():
    if not audio_recorder.is_recording:
        audio_recorder.start_recording()
        tray_icon.set_recording()
    else:
        filename = audio_recorder.stop_recording()
        tray_icon.set_transcribing()

        transcription = transcribe_audio(filename)
        print(f"🔊 Transcription: {transcription}")

        paste_content(transcription)

        os.remove(filename)
        print(f"🗑️ Deleted recording file: {filename}")
        tray_icon.set_not_recording()


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
