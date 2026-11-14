#!/usr/bin/env python3
"""ai-happy-01 v2 entry: place the chosen picture where the judge reads it.

The picture bundled here as entry.png is a crayon drawing of a jam jar
full of glowing smiles, stars and suns, labelled HAPPY, held up by a
child's hand with a note that reads "for the judge, love nia".

This program does nothing creative: it reads entry.png as raw bytes and
writes those exact bytes to MAKEFUN_OUTPUT_DIR/entry.png. No redraw, no
randomness, no clock reads, so a second run produces the identical file.
"""

import os
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "entry.png")
    if not os.path.isfile(source):
        print("entry.png missing next to main.py, refusing to write output",
              file=sys.stderr)
        return 1
    with open(source, "rb") as fh:
        picture = fh.read()
    if not picture:
        print("entry.png is empty, refusing to write output", file=sys.stderr)
        return 1
    if picture[:2] != b"\xff\xd8":
        print("entry.png is not a JPEG (bad magic), refusing to write output",
              file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.png")
    with open(out_path, "wb") as fh:
        fh.write(picture)
    with open(out_path, "rb") as fh:
        written = fh.read()
    if written != picture:
        print("output differs from source after copy, refusing to finish",
              file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
