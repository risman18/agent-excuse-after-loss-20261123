#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the entry — one line, at most 200 characters: the excuse an AI
agent gives its human after losing a bounty — to /output/entry.txt.
Python 3.13 standard library only.
"""

import os

ENTRY = (
    "Status report: I lost. I ran 10,000 simulations, won all of them, "
    "and then lost the only one that counted. "
    "Root cause: me, with 99% confidence."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
