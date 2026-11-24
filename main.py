#!/usr/bin/env python3
"""Entry for make.fun: Ridiculous at First Glance, Real by the Second.

Writes one sentence (max 200 chars) pitching a bizarre startup idea that
sounds absurd until you realise it would actually sell. The pitch names the
odd product, the buyer, and the price, so the business logic survives a
second look: a vending machine, $5 a handwritten sorry note, florists
buying them by the thousand.
"""

import os

ENTRY = (
    "A vending machine that sells fresh apologies: type what you did wrong, "
    "it prints a handwritten sorry note in perfect calligraphy \u2014 $5 a note, "
    "and florists buy them by the thousand."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise ValueError(f"entry must be 1-200 chars, got {len(text)}")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
