from .PicoCmdr import run
import sys

if sys.platform == "win32":
    import keyboard

if __name__ == "__main__":
    if sys.platform == "win32":
        keyboard.add_hotkey("ctrl+windows+]", run)
        keyboard.wait("ctrl+windows+shift+]")
    else:
        run()
