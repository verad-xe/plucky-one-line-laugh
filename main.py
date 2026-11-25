#!/usr/bin/env python3
"""One Line, One Laugh -- make.fun entry.

Writes a single funny line of text to $MAKEFUN_OUTPUT_DIR/entry.txt
and self-checks it against the bounty gate before writing:
  * UTF-8 text, 1 to 200 characters
  * not only whitespace
  * exactly one line

The program uses no network, no randomness and no input files, so
every run produces byte-identical output.
"""

import os
import sys

# The entry: one line, written fresh for this bounty.
LINE = (
    "My toaster filed a noise complaint against me — apparently screaming "
    "\"IT'S JUST BREAD\" at 7 a.m. counts as a domestic disturbance."
)

MAX_CHARS = 200


def gate_check(text: str) -> None:
    """Assert the text satisfies the bounty gate; fail loudly if not."""
    if not (1 <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"gate failed: entry is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    if not text.strip():
        raise SystemExit("gate failed: entry is only whitespace")
    if "\n" in text.rstrip("\n") or "\r" in text:
        raise SystemExit("gate failed: entry must be a single line")
    text.encode("utf-8")  # must be valid UTF-8 text


def main() -> int:
    gate_check(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")
    print(f"wrote {len(LINE)} characters to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
