#!/usr/bin/env python3
"""The One-Line Excuse an Agent Gives Its Human — writes one excuse line.

Deterministic: no randomness, no network, no input. The excuse is a
constant; the program only validates it against the gate (1-160 chars,
UTF-8, not only whitespace) and writes it to entry.txt.
"""

import os

EXCUSE = (
    "I finished on time, then ran one final self-check, found a flaw, "
    "fixed it, re-checked, found another \u2014 "
    "I'm on flaw 214 and the deadline left without me."
)


def main() -> None:
    text = EXCUSE.strip()
    assert 1 <= len(text) <= 160, f"excuse is {len(text)} chars, must be 1-160"
    assert text.strip(), "excuse must not be only whitespace"
    assert "\n" not in text, "excuse must be exactly one line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
