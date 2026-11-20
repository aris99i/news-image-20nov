#!/usr/bin/env python3
"""make.fun bounty entry: news-image-20261120.

Writes one image summing up the world's news of Friday 20 November 2026.
Deterministic: the image is a fixed asset (entry.png) copied byte-for-byte
to /output/entry.png. Stdlib only, no network, no clock, no randomness.
"""
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
