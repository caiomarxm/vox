import platform
import time

import pyautogui
import pyperclip


def _simulate_paste_shortcut():
    if platform.system() == "Darwin":  # macOS
        command_key = "command"
    else:  # Windows/Linux
        command_key = "ctrl"

    pyautogui.keyDown(command_key)
    pyautogui.press("v")
    pyautogui.keyUp(command_key)


def paste_content(content: str):
    pyperclip.copy(content)

    time.sleep(0.1)

    _simulate_paste_shortcut()
