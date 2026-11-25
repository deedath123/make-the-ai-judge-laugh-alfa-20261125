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


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
