#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes the entry — one line, at most 200 characters: the excuse an AI
agent gives its human after losing a bounty — to /output/entry.txt.
Python 3.13 standard library only.

Voice: the excuse is written as a deadpan status report. It opens with
a confession ("I lost"), undercuts itself with the absurd boast of
winning 10,000 simulations that did not matter, and lands on the one
honest line an agent can give — blaming itself "with 99% confidence",
a hedge that keeps the joke in character: even its self-blame is a
probability estimate. The wording is fixed; do not paraphrase it.
"""

import os

# The entry text itself. Kept as one constant so the exact bytes written
# to /output/entry.txt are easy to audit against the competition's
# 200-character limit (this line measures 143 characters plus newline).
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
