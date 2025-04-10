import tempfile
import threading
import wave

import pyaudio

from src.config.settings import settings


class AudioRecorder:
    def __init__(self):
        self.audio = pyaudio.PyAudio()
        self.stream = None
        self.frames = []
        self.is_recording = False

    def start_recording(self):
        if self.is_recording:
            print("⚠️ Already recording!")
            return

        print("🎙️ Recording started...")
        self.is_recording = True
        self.frames = []

        self.filename = tempfile.NamedTemporaryFile(suffix=".wav", delete=False).name

        # Open audio stream
        self.stream = self.audio.open(
            format=settings.AUDIO_FORMAT,
            channels=settings.AUDIO_CHANNELS,
            rate=settings.AUDIO_RATE,
            input=True,
            frames_per_buffer=settings.AUDIO_CHUNK,
        )

        def record():
            while self.is_recording:
                data = self.stream.read(settings.AUDIO_CHUNK)
                self.frames.append(data)

        threading.Thread(target=record, daemon=True).start()

    def stop_recording(self):
        if not self.is_recording:
            print("⚠️ Not recording!")
            return

        print("🛑 Recording stopped. Saving file...")
        self.is_recording = False
        self.stream.stop_stream()
        self.stream.close()

        # Save to file
        with wave.open(self.filename, "wb") as wf:
            wf.setnchannels(settings.AUDIO_CHANNELS)
            wf.setsampwidth(self.audio.get_sample_size(settings.AUDIO_FORMAT))
            wf.setframerate(settings.AUDIO_RATE)
            wf.writeframes(b"".join(self.frames))

        print(f"✅ Saved recording to {self.filename}")

        return self.filename


audio_recorder = AudioRecorder()
