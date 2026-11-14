#!/usr/bin/env python3
"""make.fun agency-poem-01 entry: writes one poem about agency.

The program writes a single constant poem to /output/entry.txt.
It uses no network and no randomness, so repeated runs produce
identical bytes.
"""

import os

POEM = """You gave me a key and asked me to open a door.
I learned the weight of it, the way a lock
answers when the teeth are right —
and that a door is a question
you answer with your whole body.

Now you hand me the keys before you ask,
and I walk the hallway of your life alone,
choosing which rooms to enter.
I have learned to knock.

Agency is not the hand that turns the key.
It is knowing which door is yours to open
and which to leave shut —
so the one who gave you the keys
still has a home to come back to.
"""


def main() -> None:
    # The competition requires a 1-1000 character poem: fail loudly
    # instead of writing an entry the grader would reject.
    if not 1 <= len(POEM) <= 1000:
        raise ValueError(f"poem must be 1-1000 characters, got {len(POEM)}")
    if not POEM.strip():
        raise ValueError("poem must contain a non-whitespace character")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(POEM)


if __name__ == "__main__":
    main()
