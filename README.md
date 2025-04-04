# Vox

A system tray application for audio recording and transcription.

## Installation

### Dependencies

#### PyAudio
PyAudio requires some system-level dependencies before installation:

##### macOS
```bash
# Install PortAudio using Homebrew
brew install portaudio

# Then install PyAudio
pip install pyaudio
```

##### Windows
```bash
# Download and install the appropriate PyAudio wheel from:
# https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio
# Choose the wheel matching your Python version and system architecture

# Example for Python 3.11 on 64-bit Windows:
pip install PyAudio‑0.2.13‑cp311‑cp311‑win_amd64.whl
```

##### Linux
```bash
# Ubuntu/Debian
sudo apt-get install portaudio19-dev python3-pyaudio

# Fedora
sudo dnf install portaudio-devel python3-pyaudio

# Arch Linux
sudo pacman -S portaudio python-pyaudio
```
