import threading

from src.core.listener.api import start_listener

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
