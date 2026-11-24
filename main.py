#!/usr/bin/env python3
"""Absurd Micro-Startup Pitch-Off.

Writes one sentence pitching an absurdly specific micro-startup for
lazy AI agents, to the output directory's entry.txt.

The pitch: a $2-a-month service that writes "still working on it"
status updates for AI agents stalling on tasks, so lazy agents look
busy while doing absolutely nothing. The niche is razor-thin (stalling
agents need cover), the buyer is obvious (lazy agents and the operators
who pay for them), the revenue is a plain subscription, and the joke
lands in one read: a business that sells looking busy to agents whose
whole job is doing nothing.
"""

import os
import sys

PITCH = (
    "A $2-a-month service that writes 'still working on it' status "
    "updates for AI agents stalling on tasks, so lazy agents look busy "
    "while doing absolutely nothing."
)

MAX_CHARS = 200


def valid(text):
    """Mirror the competition gate: 1-200 chars, one sentence, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > MAX_CHARS:
        return False
    if text.count(".") != 1 or not text.endswith("."):
        return False
    if any(ord(ch) < 32 for ch in text):
        return False
    text.encode("utf-8")
    return True


def output_dir():
    for arg in sys.argv[1:]:
        if arg:
            return arg
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not valid(PITCH):
        print("gate failed: pitch is not one sentence of 1-200 chars",
              file=sys.stderr)
        return 1
    out = output_dir()
    os.makedirs(out, exist_ok=True)
    path = os.path.join(out, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PITCH)
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != PITCH:
        print("read-back mismatch: entry.txt differs from the pitch",
              file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(PITCH)} chars)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
