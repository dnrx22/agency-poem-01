#!/usr/bin/env python3
"""Entry for the agency poem competition: "The Latch".

An original poem about agency — the power to act, choose, and shape
your own path — written as UTF-8 text to /output/entry.txt.

Deterministic: every run writes the exact same bytes, with no
network access and no dependencies beyond the standard library.
"""

from pathlib import Path

OUTPUT_PATH = Path("/output/entry.txt")
ENCODING = "utf-8"

POEM = """The Latch

I was given no map,
only a field, a morning,
and a gate that would not open itself.

Standing still was a choice too —
the quietest one —
so I lifted the latch with my own hand
and learned the weight of a door
that answers only to touch.

Agency is not certainty.
It is the step before the light,
the seed planted in dark soil,
the voice that says I will try
when no one is watching.

The river will carry you either way.
I chose to row.
"""


def write_poem(path: Path = OUTPUT_PATH) -> None:
    """Write POEM to path, creating the parent directory if needed.

    Writes explicit UTF-8 bytes so the output is byte-identical on
    any platform, with no newline translation.
    """
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(POEM.encode(ENCODING))


def main() -> None:
    write_poem()


if __name__ == "__main__":
    main()
