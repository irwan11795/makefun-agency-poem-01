# Agency poem v2 (make.fun agency-poem-01).
#
# The simplest entry the rules allow: a repository holding a program that
# writes one poem to /output/entry.txt. The poem is an original work about
# agency — the power to choose and to act, and what happens when you hand
# the writing to an agent but keep the sending for yourself. The agent
# drafts the apology, picks the hour, parks the cursor; the speaker's
# finger is the last inch of agency, because pressing Send is what turns
# a draft into a deed. The program does no drawing, no network and no
# randomness: it writes the same bytes every run.

import os
import sys

POEM = """The Last Inch

It wrote the email in my voice,
every sorry in the right place,
every sentence sanded smooth.

It even chose the hour to send it,
when my sister would be awake and kind,
and parked the cursor on Send.

All I have to do is press.
One inch. One small blue word.
My finger has been hovering an hour.

Because the moment I press it
the words stop being a draft
and start being mine.

It can write the sorry.
Only I can be sorry.
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
