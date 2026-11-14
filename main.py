# Agency poem v1 (make.fun agency-poem-01).
#
# The simplest entry the rules allow: a repository holding a program that
# writes one poem to /output/entry.txt. The poem is an original work about
# agency — the power to choose and to act, and what happens when you hand
# that power to another (here, an agent that acts for you). The program
# does no drawing, no network and no randomness: it writes the same bytes
# every run.

import os
import sys

POEM = """The Signature

I taught it to sign my name,
the loops, the slant, the small lift at the end,
until the ink forgot whose hand it was.

Now it signs while I sleep:
letters, forms, the small permissions
that keep a life moving.

This morning I watched it sign a letter
I had not read, in my name, in my hand,
and the signature was perfect.
Steadier than mine has ever been.

I stood there holding the pen I no longer needed
and understood at last:
my name was never my hand.
It was my yes.
"""


def write_poem(path):
    """Write the poem to path as UTF-8 and verify the bytes round-trip.

    Returns the number of characters written. Fails loudly if the file
    does not come back byte-identical, so a truncated write is never
    shipped silently.
    """
    data = POEM.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("entry.txt did not round-trip byte-identical")
    if not any(not ch.isspace() for ch in POEM):
        raise SystemExit("entry.txt holds no non-whitespace character")
    return len(POEM)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    write_poem(dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
