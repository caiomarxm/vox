import pystray
from PIL import Image, ImageDraw


class TrayIcon:
    def __init__(self):
        self._icon = None
        self._is_recording = False
        self._create_icon()

    def _create_icon(self):
        # Create menu items
        menu = (pystray.MenuItem("Exit", self._exit),)

        # Create the icon with initial normal state
        self._icon = pystray.Icon(
            "vox", self._create_normal_icon(), "Vox - Audio Recorder", menu
        )

    def set_recording(self):
        """Set the tray icon to recording state."""
        self._is_recording = True
        if self._icon:
            self._icon.icon = self._create_recording_icon()

    def set_not_recording(self):
        """Set the tray icon to not recording state."""
        self._is_recording = False
        if self._icon:
            self._icon.icon = self._create_normal_icon()

    def _create_normal_icon(self):
        image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))  # Transparent background
        draw = ImageDraw.Draw(image)

        # Draw microphone body (white circle)
        draw.ellipse((20, 10, 44, 34), fill="white", outline="black")

        # Draw microphone handle (white rectangle)
        draw.rectangle((28, 34, 36, 50), fill="white", outline="black")

        return image

    def _create_recording_icon(self):
        image = Image.new("RGBA", (64, 64), (0, 0, 0, 0))  # Transparent background
        draw = ImageDraw.Draw(image)

        # Draw microphone body (white circle)
        draw.ellipse((20, 10, 44, 34), fill="white", outline="black")

        # Draw microphone handle (white rectangle)
        draw.rectangle((28, 34, 36, 50), fill="white", outline="black")

        # Draw small red dot for recording indicator
        draw.ellipse((48, 6, 56, 14), fill="red")

        return image

    def _exit(self):
        self._icon.stop()

    def run(self):
        """Start the tray icon."""
        self._icon.run()


tray_icon = TrayIcon()
