#!/usr/bin/env python3
"""The Dog Reviews the Mailman — one-line entry.

Writes a single funny one-line review from a dog about the mailman
to /output/entry.txt (gate: 1-200 characters).
"""

import os

LINE = "Five stars last Tuesday — he slipped me a biscuit through the gate. Today: paper again. One star. Dogs remember."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(f"{len(LINE)} chars: {LINE}")


if __name__ == "__main__":
    main()
