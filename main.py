#!/usr/bin/env python3
"""Make the AI Judge Laugh (u-alfasurya91 edition) — entry program.

Writes one office-life joke, a single line under 200 characters, to
/output/entry.txt. Python 3.13 standard library only; no network, no input.
"""

import os

ENTRY = (
    "The coffee machine died at 8:03, so by 9:15 twelve engineers had built "
    "a queue, a spreadsheet, and a Slack channel \u2014 and the intern fixed "
    "it by plugging it back in."
)


def _validate(text: str) -> None:
    """Gate guard: the entry must be 1-200 chars of non-blank UTF-8 text."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry length {len(text)} outside 1-200 chars")
    if not text.strip():
        raise ValueError("entry is only whitespace")
    text.encode("utf-8")


def main() -> None:
    _validate(ENTRY)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
