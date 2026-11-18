"""news-image-20261117 entry: copy the front page to the output dir.

The image (entry.png, 1024x1024) is a newspaper front page summing
up Tuesday 17 November 2026: 30 numbered stories in the 30-story
front-page layout — a masthead with the date, 3 illustrated leads,
8 illustrated cards, a "Where it happened" world map and an "Also
on" list, plus a sources footer. This program only copies it, byte
for byte, so both runs write identical bytes. No network, standard
library only.
"""

import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    # Byte-for-byte copy: deterministic by construction.
    shutil.copyfile(HERE / "entry.png", OUT / "entry.png")


if __name__ == "__main__":
    main()
