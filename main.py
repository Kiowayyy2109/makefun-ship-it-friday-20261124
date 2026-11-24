"""Ship It Friday entry: write the one-line commit message to /output/entry.txt.

The line is the funniest git commit message an AI coding agent writes in the
moment before it breaks production on a Friday: 4:59pm, billing refactor,
laptop already closed.
"""

import hashlib
import os
from pathlib import Path

TEXT = "feat: it's 4:59pm on a Friday, I refactored the billing code, and I have already closed my laptop — good luck, prod!"


def main() -> None:
    assert 1 <= len(TEXT) <= 159, len(TEXT)
    assert TEXT.strip() == TEXT and "\n" not in TEXT and "\r" not in TEXT
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    out = out_dir / "entry.txt"
    data = TEXT.encode("utf-8")
    assert b"\n" not in data and not data.endswith(b"\n")
    out.write_bytes(data)
    print(len(TEXT))
    print(hashlib.sha256(TEXT.encode("utf-8")).hexdigest())


if __name__ == "__main__":
    main()
