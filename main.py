"""Entry for the make.fun bounty "Sum up 22 November's world news in one image"
(https://make.fun/bounty/news-image-20261122).

The entry image is a newspaper front page summarising the world's news of
Sunday 22 November 2026, made for this bounty and held in this repository as
entry.png (1024x1024, under 1 MiB). Its four stories, checked against the
day's reporting:

  - COP31 climate talks in Antalya, Turkiye, collapse with no agreement
    after a dispute over fossil fuels.
  - The International Court of Justice rules that Myanmar committed
    genocide against its Rohingya minority.
  - Tankers are attacked near the Strait of Hormuz; Bahrain reports an
    Iranian attack on an industrial facility.
  - Russian strikes hit an apartment building near Kyiv as winter nears.

The strip at the foot also notes the US questioning Nvidia's AI-chip sales
to China, the Nigeria boat tragedy, and the Indonesia factory fire.

The program copies entry.png byte-for-byte to /output/entry.png, so both
runs write identical bytes and no network is needed.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    print("wrote %s (%d bytes)" % (DST, os.path.getsize(DST)))


if __name__ == "__main__":
    main()
