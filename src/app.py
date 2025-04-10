import threading

from src.core.listener.api import start_listener
from src.core.system.tray import tray_icon

# Run listener in a thread so it doesn't block main thread
listener_thread = threading.Thread(target=start_listener, daemon=True)
listener_thread.start()

# Start the tray icon
print("🔍 Listening for hotkey... Press Ctrl + Space to trigger.")
tray_icon.run()
