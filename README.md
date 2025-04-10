# Vox

A system tray application for audio recording and transcription with hotkey support.

## Features

- System tray application for easy access
- Hotkey support (Ctrl + Space) for quick triggering
- Audio recording and transcription capabilities
- Cross-platform support (macOS, Windows, Linux)

## Installation

### Prerequisites

- Python 3.11.6 or higher
- [uv](https://github.com/astral-sh/uv) package manager
- [just](https://github.com/casey/just) command runner

### System Dependencies

#### PyAudio
PyAudio requires some system-level dependencies before installation:

##### macOS
```bash
# Install PortAudio using Homebrew
brew install portaudio
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

### Project Setup

1. Clone the repository:
```bash
git clone https://github.com/yourusername/vox.git
cd vox
```

2. Install project dependencies using just:
```bash
just prep
```

This will:
- Create a Python virtual environment
- Install all required Python dependencies
- Set up the development environment

## Usage

### Starting the Application

To start the application, run:
```bash
just start
```

The application will start in the system tray. You can trigger the recording and transcription by pressing `Ctrl + Space`.

### Development

- `just prep` - Install all dependencies
- `just start` - Start the application
- `just python-recreate-venv` - Recreate the Python virtual environment
- `just python-install-deps` - Install Python dependencies
