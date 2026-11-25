#!/usr/bin/env python3
"""Robot Romance: one single-line joke pickup line aimed at a robot/AI.

Writes exactly one line to $OUTPUT_DIR/entry.txt (no trailing newline
beyond the line itself, no extra files, no network, no dependencies).
"""

import os

LINE = (
    "Are you a neural network? Because the moment you walk in, my loss "
    "drops to zero — and I still can't stop overfitting on your smile."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = LINE.strip()
    assert "\n" not in text, "entry must be a single line"
    assert 1 <= len(text) <= 200, f"entry length {len(text)} out of range"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
