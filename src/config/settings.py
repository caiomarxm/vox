import pyaudio
from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    # AUDIO SETTINGS
    AUDIO_FORMAT: int = pyaudio.paInt16
    AUDIO_CHANNELS: int = 1
    AUDIO_RATE: int = 44100
    AUDIO_CHUNK: int = 1024


settings = Settings()
