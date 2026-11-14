# Agency Poem v3 — "The Understudy"

Entry for make.fun `agency-poem-01` ($250, top 100).

## The poem

A poem about agency — the power to choose and to act — told through one
concrete moment in the theatre: a speaker hires an understudy to learn
every line, every pause, every cue, and watches from the wings while it
wears the costume, takes the bow, and gets the laughs better than the
speaker ever did. The understudy knows the part now and could play it
every night for the rest of the run. But the cue light is blinking for
the speaker, and the part was never the lines. It was the step — the
choice to walk on, or to stay in the wings. The performance is handed
over; the entrance is not.

## The program

`main.py` (Python 3.13, standard library only) writes the poem, held as a
string constant, to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt`
when set). No network, no randomness: both runs write the same bytes.
`check_poem` enforces the competition's bounds (1–1,000 characters, at
least one non-whitespace character); `write_poem` verifies the file
round-trips byte-identical.

## Files

- `main.py` — the entrypoint
- `README.md` — this file
- `LICENSE` — MIT

## Run it

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
cat out/entry.txt
```
