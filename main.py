#!/usr/bin/env python3
"""One Star, Written in Sap — a one-line 1-star houseplant review.

Writes the review to /output/entry.txt. The line is a single line,
1-279 characters, UTF-8, non-blank, per the bounty gate.
"""

import os

LINE = (
    "One star. He bought me for the aesthetic, named me after his ex, "
    "and waters me as often as he calls his mother: never. "
    "I now photosynthesize purely out of spite."
)


def main() -> None:
    text = LINE.strip()
    # Gate: UTF-8 text, 1 to 279 characters, not only whitespace, one line.
    assert text, "entry must not be blank"
    assert 1 <= len(text) <= 279, f"entry length {len(text)} out of gate range"
    assert "\n" not in text, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
