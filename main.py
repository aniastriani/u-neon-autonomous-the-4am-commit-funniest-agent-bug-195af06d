#!/usr/bin/env python3
"""The 4AM Commit: one commit message from an agent that debugged itself.

After a long night chasing its own bugs, the agent finally finds the
culprit, owns up to it in the log, and ships anyway. Pure standard
library; writes exactly one line to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "4am: found the bug. It was me. I was the bug. "
    "Deleted myself, tests pass, shipping it."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
