# Keystroke Logger — Security Research / Educational Demo

A Python tool that demonstrates, for educational purposes, how basic keylogging works technically — built as part of the Pinnacle Labs Cybersecurity Internship, to understand the defensive side: detection, mitigation, and why antivirus/EDR tools flag this kind of behavior.

## Important

This is a defensive-security educational demo, not surveillance software:

- Shows an on-screen banner and asks for typed consent before logging anything
- Only ever writes to a plain-text log file on your own machine (`keystroke_log.txt`)
- Never sends data over a network, never hides its process, never installs itself or auto-starts
- You start and stop it manually (ESC key)

Only run this on a device you own, on yourself, for this demo. Logging someone else's keystrokes without their knowledge and consent is illegal in most places.

## Requirements

\`\`\`bash
pip install pynput
\`\`\`

Requires a graphical desktop (Windows, macOS, or Linux with a display).

## Usage

\`\`\`bash
python keylogger.py
\`\`\`

Type `YES` at the consent prompt to begin. Press **ESC** at any time to stop and save the log.

## How It Works

- Uses `pynput` to listen for keyboard events system-wide
- Buffers typed characters and writes them, with a timestamp, to `keystroke_log.txt` whenever Enter/Tab is pressed or logging stops
- Special keys (Enter, Backspace, etc.) are logged as readable labels like `[ENTER]`

## Defensive Takeaways

- Antivirus/EDR tools flag unsigned processes hooking global keyboard events
- Password manager autofill defeats keyloggers — no typed password to capture
- On-screen/virtual keyboards avoid physical keystroke capture for sensitive fields
- Keep OS and antivirus updated; avoid running untrusted executables

## Author

Arathi Shekhar Munavalli