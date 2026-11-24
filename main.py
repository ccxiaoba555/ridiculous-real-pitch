#!/usr/bin/env python3
"""Ridiculous at First Glance, Real by the Second.

Pitches a bizarre startup idea that sounds absurd until you realise it
would actually sell: a dog-walking service for people who do not own a
dog. First draft ended on "keep your freedom", which only sold the
renter's side; the tighter cut names the turn -- the owner gets a
walked dog, you skip the vet bills -- so both sides of the market are
visible in one sentence. The absurd half is paying to walk someone
else's dog; the real half is that dog owners need walkers and dog-less
people want dogs without the commitment.
"""

import os

PITCH = (
    "A dog-walking service for people who don't own a dog: rent a "
    "stranger's dog by the hour, get the walk and the cuddles, then "
    "hand the leash back -- the owner gets a walked dog, you skip "
    "the vet bills."
)

OUTPUT_PATH = os.path.join(os.environ.get("OUTPUT_DIR", "/output"), "entry.txt")


def validate(text: str) -> str:
    """Enforce the gate: one sentence, 1-200 chars of UTF-8, not blank."""
    text = text.strip()
    if not text:
        raise ValueError("pitch must not be empty or only whitespace")
    if len(text) > 200:
        raise ValueError(f"pitch is {len(text)} chars, over the 200 limit")
    if "\n" in text or "\r" in text:
        raise ValueError("pitch must be a single line")
    if text.count(".") != 1 or not text.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    text.encode("utf-8")  # must be valid UTF-8 text
    return text


def main() -> None:
    text = validate(PITCH)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    # Read it back: the file must hold exactly the pitch, one sentence.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != text:
        raise ValueError("entry.txt does not hold exactly the pitch")
    print(f"wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
