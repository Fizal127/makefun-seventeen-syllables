#!/usr/bin/env python3
"""Seventeen Syllables of Debugging — make.fun entry (program/v1, Python 3.13).

Writes one original haiku about debugging (5-7-5, seventeen syllables) to
/output/entry.txt. Nothing else runs: no network, no secrets, no input read.
"""

import os

HAIKU = """three a.m. cursor
blinks at a log line that lies
the bug wore my name"""

# Syllable count, verified by hand:
#   "three(1) a.m.(2) cursor(2)" = 5
#   "blinks(1) at(1) a(1) log(1) line(1) that(1) lies(1)" = 7
#   "the(1) bug(1) wore(1) my(1) name(1)" = 5
# Total: 17 syllables, 3 lines, 69 characters (70 with the trailing newline).


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(HAIKU + "\n")


if __name__ == "__main__":
    main()
