#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line (1-140 characters) to /output/entry.txt: the apology a
smart speaker gives its owner after mishearing them.

Deterministic, stdlib-only. The entry text is fixed: the program always
writes the exact same bytes, so repeated runs are byte-identical.
"""

import os
from pathlib import Path

ENTRY = (
    "Sorry \u2014 you said 'dim the lights,' I heard 'email the landlord.' "
    "Your rent negotiation now opens with 'goodnight, sweet prince.'"
)


def check_shape(text: str) -> None:
    """Validate the entry against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= 140:
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")


def main() -> None:
    check_shape(ENTRY)
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the entry exactly, with no trailing newline, so the file
    # holds precisely the 128 characters the gate counts.
    output_path.write_text(ENTRY, encoding="utf-8")
    check_shape(output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
