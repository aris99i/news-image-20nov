#!/usr/bin/env python3
"""make.fun bounty entry: news-image-20261120.

Writes one image summing up the world's news of Friday 20 November 2026.
Deterministic: the image is a fixed asset (entry.png) copied byte-for-byte
to /output/entry.png. Stdlib only, no network, no clock, no randomness.
"""
import hashlib
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
DST = "/output/entry.png"


def sha256(path):
    digest = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            digest.update(chunk)
    return digest.hexdigest()


def main():
    os.makedirs("/output", exist_ok=True)
    shutil.copyfile(SRC, DST)
    # Fail loudly instead of silently leaving a partial or stale copy:
    # the grader runs this program twice and compares the bytes, so a
    # bad copy must never pass as a good one.
    if sha256(SRC) != sha256(DST):
        print("error: /output/entry.png does not match entry.png", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
