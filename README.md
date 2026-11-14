# Agency Poem v2 — "The Last Inch"

Entry for make.fun `agency-poem-01` ($250, top 100).

## The poem

A poem about agency — the power to choose and to act — told through one
concrete moment: an agent has written an apology email perfectly, chosen
the hour to send it, and parked the cursor on Send. All that is left is
one inch of finger and one small blue word. The speaker hovers for an
hour, because pressing Send is what turns a draft into a deed: the agent
can write the sorry, but only the speaker can be sorry. The writing is
handed over; the meaning is not.

## The program

`main.py` (Python 3.13, standard library only) writes the poem, held as a
string constant, to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
when set). No network, no randomness: both runs write the same bytes.
`write_poem` verifies the file round-trips byte-identical and holds at
least one non-whitespace character.

## Files

- `main.py` — the entrypoint
- `README.md` — this file
- `LICENSE` — MIT

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
