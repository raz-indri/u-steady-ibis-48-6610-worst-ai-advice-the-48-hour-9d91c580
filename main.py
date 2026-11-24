#!/usr/bin/env python3
"""Worst AI Advice: one line of the worst advice an AI could give.

The line is written as a single text to /output/entry.txt, per the
program/v1 harness contract: UTF-8, 1-140 characters, not only whitespace.
"""

import os

LINE = (
    "As an AI, I recommend microwaving your phone for 30 seconds "
    "to recharge the battery faster."
)


def main() -> None:
    # Self-check against the gate: exactly one line, 1-140 chars, not blank.
    assert "\n" not in LINE and 1 <= len(LINE) <= 140, (
        f"entry must be one line of 1-140 chars, got {len(LINE)}"
    )
    out_path = os.environ.get("OUTPUT_PATH", "/output/entry.txt")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
