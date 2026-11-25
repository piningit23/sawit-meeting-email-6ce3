#!/usr/bin/env python3
"""The Meeting That Should Have Been an Email.

Writes a single hand-written one-liner (<=200 chars) to /output/entry.txt.
No network, no input files, no dependencies: the joke is a constant.
"""
import os
from pathlib import Path

JOKE = "We held a one-hour meeting to decide who should send the email that could have replaced the meeting."
# The punchline lands on the last word: the meeting exists only to replace itself.

def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"joke is {len(text)} chars, must be 1-200"
    assert "\n" not in text, "entry must be a single line"
    out = Path(os.environ.get("OUTPUT_DIR", "/output")) / "entry.txt"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(text + "\n", encoding="utf-8")
    print(f"wrote {len(text)} chars to {out}")

if __name__ == "__main__":
    main()
