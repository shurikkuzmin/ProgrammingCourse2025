# Minimal Pygame Example

This project contains a tiny `pygame` example showing a window with a movable circle.

Quick start

1. Create a virtual environment (optional but recommended):

```bash
python3 -m venv .venv
source .venv/bin/activate
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the example:

```bash
python3 pygame_example.py
```

Controls: arrow keys to move the circle, Esc or close window to quit.

Notes:
- On some Linux systems you may need to install system dependencies (SDL development libs) before installing `pygame`.
- If you only want to test without installing, you can read the `pygame_example.py` file to see the minimal loop.
