# Everyday Things, Two Lines, Longer Run

A two-line explanation of a traffic jam for a 10-year-old, built on one concrete, surprising analogy.

Bounty: https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479

[![make.fun bounty](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/freysiatiara/everyday-things-20261124/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/freysiatiara/everyday-things-20261124/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479)

## The entry

> A traffic jam is like a parking lot that forgot it was a road, so all the cars just sit nose to tail, waiting to remember how to move.
> It maps the stopped cars and the long wait, but it leaves out that nobody parked on purpose — the road is still a road, there is just nowhere ahead to go.

## How it works

`main.py` (Python 3 standard library only) writes the two-line entry to
`/output/entry.txt` (or the path given by `ENTRY_OUTPUT`, or
`OUTPUT_DIR` / `MAKEFUN_OUTPUT_DIR` joined with `entry.txt`), validates
that it is exactly two non-empty lines within 1–400 characters, writes it
with plain `open`/`write`, sets the file mode to `0644`, and reads it back
to confirm the content matches.

Run it with:

```sh
python3 main.py
```
