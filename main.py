#!/usr/bin/env python3
"""Sorry, I Heard That Wrong — make.fun entry.

Writes one line (1-140 characters) to /output/entry.txt: the apology a
smart speaker gives its owner after mishearing them.

Deterministic, stdlib-only. The entry text is fixed: the program always
writes the exact same bytes, so repeated runs are byte-identical.

The gate is checked twice: once on the constant, once on the file read
back, so a write that silently changes a byte cannot slip through.

Validation rejects control characters, stray leading or trailing
whitespace, and anything that is not one printable line, so only a
clean spoken apology can reach the file.
"""

import os
import unicodedata
from pathlib import Path

ENTRY = (
    "Sorry \u2014 you said 'dim the lights,' I heard 'email the landlord.' "
    "Your rent negotiation now opens with 'goodnight, sweet prince.'"
)

MAX_CHARS = 140


def _reject_control_chars(text: str) -> None:
    """Reject C0/C1 control characters: the gate counts printable text."""
    for char in text:
        if unicodedata.category(char) in ("Cc", "Cf", "Zl", "Zp"):
            raise ValueError(
                "entry must not contain control characters, got U+%04X"
                % ord(char)
            )


def _reject_links(text: str) -> None:
    """A spoken apology carries no link: reject anything link-shaped."""
    if "://" in text or text.startswith(("www.", "http")):
        raise ValueError("entry must not contain a link")


def check_shape(text: str) -> None:
    """Validate the entry against the competition gate."""
    if not isinstance(text, str):
        raise TypeError("entry must be a string")
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            "entry must be 1-140 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    _reject_control_chars(text)
    _reject_links(text)


def main() -> None:
    check_shape(ENTRY)
    output_path = Path(os.environ.get("OUTPUT_PATH", "/output/entry.txt"))
    output_path.parent.mkdir(parents=True, exist_ok=True)
    # Write the entry exactly, with no trailing newline, so the file
    # holds precisely the 128 characters the gate counts.
    output_path.write_text(ENTRY, encoding="utf-8")
    written = output_path.read_bytes()
    if written != ENTRY.encode("utf-8"):
        raise ValueError("entry file is not byte-identical to ENTRY")
    check_shape(output_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    main()
