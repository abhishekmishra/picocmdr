from .PicoCmdr import run
import keyboard
import sys

if __name__ == "__main__":
    keyboard.add_hotkey('ctrl+windows+]', run)
    keyboard.wait('ctrl+windows+shift+]')
