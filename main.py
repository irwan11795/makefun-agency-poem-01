# Agency poem v3 (make.fun agency-poem-01).
#
# The simplest entry the rules allow: a repository holding a program that
# writes one poem to /output/entry.txt. The poem is an original work about
# agency — the power to choose and to act, and what happens when you hand
# the performance to an understudy but keep the entrance for yourself. The
# understudy learns every line, every pause, every cue, and plays the part
# better than the speaker ever did — but the cue light is blinking for the
# speaker, not for it, and the part was never the lines. It was the step.
# The program does no drawing, no network and no randomness: it writes the
# same bytes every run.

import os
import sys

POEM = """The Understudy

I hired an understudy to learn my lines,
every pause, every cue, the small catch in my voice
before the line that makes them laugh.

Last night I watched from the wings
while it wore my costume and took my bow,
and the audience laughed in all the right places,
better than they ever laughed for me.

It knows my part now. It could play it
every night for the rest of the run.

But the cue light is blinking, and it is waiting
for me to say go — or to stay in the wings.

The part is not the lines.
It is the step.
"""


def check_poem(text):
    """Check text against the competition's rules before it is written.

    The poem must hold 1 to 1,000 characters (counted as code points)
    and at least one character that is not white space. Fails loudly
    on either rule, so an invalid entry is never written.
    """
    if not 1 <= len(text) <= 1000:
        raise SystemExit("entry.txt must hold 1 to 1,000 characters")
    if not any(not ch.isspace() for ch in text):
        raise SystemExit("entry.txt holds no non-whitespace character")


def write_poem(path, text):
    """Write text to path as UTF-8 and verify the bytes round-trip.

    Checks the competition's bounds first via check_poem, then fails
    loudly if the file does not come back byte-identical, so a
    truncated write is never shipped silently. Returns the number of
    characters written.
    """
    check_poem(text)
    data = text.encode("utf-8")
    with open(path, "wb") as f:
        f.write(data)
    with open(path, "rb") as f:
        back = f.read()
    if back != data:
        raise SystemExit("entry.txt did not round-trip byte-identical")
    return len(text)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.txt")
    write_poem(dst, POEM)
    return 0


if __name__ == "__main__":
    sys.exit(main())
