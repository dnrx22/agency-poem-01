#!/usr/bin/env python3
"""Write the agency poem to /output/entry.txt.

Deterministic: every run writes the exact same UTF-8 bytes.
Standard library only, no network.
"""

from pathlib import Path

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


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
