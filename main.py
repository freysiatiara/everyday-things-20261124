"""Everyday Things, Two Lines, Longer Run — make.fun bounty entry.

Writes the two-line entry to the output path, resolved in this order:
  1. ENTRY_OUTPUT environment variable
  2. OUTPUT_DIR / MAKEFUN_OUTPUT_DIR joined with "entry.txt"
  3. /output/entry.txt

Standard library only.
"""

import os

ENTRY_TEXT = (
    "A traffic jam is like a parking lot that forgot it was a road, "
    "so all the cars just sit nose to tail, waiting to remember how to move.\n"
    "It maps the stopped cars and the long wait, but it leaves out that "
    "nobody parked on purpose \u2014 the road is still a road, there is just "
    "nowhere ahead to go.\n"
)


def resolve_output_path():
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        base = os.environ.get(var)
        if base:
            return os.path.join(base, "entry.txt")
    return "/output/entry.txt"


def main():
    text = ENTRY_TEXT
    if not text or not text.strip():
        raise SystemExit("entry text is empty or whitespace-only")
    if not 1 <= len(text) <= 400:
        raise SystemExit(
            "entry text must be 1..400 characters, got %d" % len(text)
        )
    lines = text.rstrip("\n").split("\n")
    if len(lines) != 2:
        raise SystemExit("entry text must be exactly two lines, got %d" % len(lines))
    if any(not line.strip() for line in lines):
        raise SystemExit("entry lines must not be empty or whitespace-only")
    if any(line != line.strip() for line in lines):
        raise SystemExit(
            "entry lines must not have leading or trailing whitespace"
        )

    path = resolve_output_path()
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="") as f:
        read_back = f.read()
    if read_back != text:
        raise SystemExit("verification failed: file content differs from entry text")
    print("wrote %s (%d characters)" % (path, len(text)))


if __name__ == "__main__":
    main()
