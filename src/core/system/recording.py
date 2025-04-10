import threading
import wave

import pyaudio

#
# Audio settings
#

# TODO: Make these configurable
FORMAT = pyaudio.paInt16
CHANNELS = 1
RATE = 44100
CHUNK = 1024
FILENAME = "recorded_audio.wav"

# Global variables
# TODO: Move these to a class
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

    return FILENAME
