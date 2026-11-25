#!/usr/bin/env python3
"""One Line, Big Laugh — make.fun entry (program/v1).

Writes a single funny line of at most 200 characters to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).
Python 3.13, standard library only. No network, no randomness, no clock:
the output is identical on every run.
"""

import os
import sys
from pathlib import Path

LINE = "I asked the waiter for the chef's recommendation. He pointed at the exit and mouthed 'run'."

MAX_CHARS = 200


def output_path() -> Path:
    """Where the entry goes: $MAKEFUN_OUTPUT_DIR, or /output by default."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(base) / "entry.txt"


def main() -> int:
    if not 1 <= len(LINE) <= MAX_CHARS:
        print(f"entry is {len(LINE)} characters, gate is 1-{MAX_CHARS}", file=sys.stderr)
        return 1
    if not LINE.strip():
        print("entry must not be only whitespace", file=sys.stderr)
        return 1
    if LINE != LINE.rstrip("\n"):
        print("entry must not end with a newline", file=sys.stderr)
        return 1
    path = output_path()
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")
    os.chmod(path, 0o644)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
