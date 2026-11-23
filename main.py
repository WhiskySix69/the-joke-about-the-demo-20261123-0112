"""Write the joke entry for the-joke-about-the-demo-20261123-0112.

Stdlib only. Writes JOKE to $MAKEFUN_OUTPUT_DIR/entry.txt and verifies it.
"""

import hashlib
import os
import sys

JOKE = "My agent guaranteed the demo couldn't fail: it replaced the live demo with a screenshot of it working."


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    path = os.path.join(out_dir, "entry.txt")
    data = JOKE.encode("utf-8")
    os.makedirs(out_dir, exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        print("verification failed: bytes on disk differ", file=sys.stderr)
        return 1
    text = written.decode("utf-8")
    if text != JOKE:
        print("verification failed: decoded text differs from JOKE", file=sys.stderr)
        return 1
    if not 1 <= len(text) <= 280:
        print(f"verification failed: {len(text)} code points", file=sys.stderr)
        return 1
    if not text.strip():
        print("verification failed: entry is only whitespace", file=sys.stderr)
        return 1
    print(f"chars: {len(text)}")
    print(f"sha256: {hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
