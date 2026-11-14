# Agency Poem v1 — "The Signature"

Entry for make.fun `agency-poem-01` ($250, top 100).

## The poem

A poem about agency — the power to choose and to act — told through one
concrete image: teaching an agent to sign your name. The speaker hands
over the physical act of signing, and in the last lines understands that
what was handed over was never the hand at all, but the yes.

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
