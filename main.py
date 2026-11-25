"""Fix Human Sleep: Funniest Patch Note.

Writes one line of patch notes to $MAKEFUN_OUTPUT_DIR/entry.txt
announcing that human sleep has been fixed: the alarm used to go
off before sleep had finished installing, and now sleep completes
before the alarm is allowed to ring. Standard library only.
"""

import os
import sys

PATCH_LINE = (
    "Fixed a bug where the alarm went off before sleep had "
    "finished installing. Sleep now completes before the alarm "
    "is allowed to ring."
)


def patch_gate(text):
    """Check the patch note against the competition gate.

    The gate wants plain UTF-8 text of 1 to 160 characters, not
    only white space, on a single line: one patch note announcing
    a fix for human sleep, funny enough to laugh at and plausible
    enough to sit in a real changelog. Returns the cleaned text
    or raises ValueError.
    """
    cleaned = text.strip()
    if not cleaned:
        raise ValueError("patch note must not be only whitespace")
    if len(cleaned) > 160:
        raise ValueError(
            "patch note is %d characters, over the 160 limit"
            % len(cleaned)
        )
    if "\n" in cleaned or "\r" in cleaned:
        raise ValueError("patch note must be exactly one line")
    return cleaned


def patch_measure(text):
    """Measure the patch note for one last sanity pass.

    Returns a dict with the character count and the word count of
    the cleaned text. A note too short to carry both the fix and
    the joke, or one padded out to fill the cap instead of landing
    the punchline, is caught here before anything is written.
    """
    words = text.split()
    return {"chars": len(text), "words": len(words)}


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    text = patch_gate(PATCH_LINE)
    shape = patch_measure(text)
    if shape["words"] < 5:
        raise ValueError("patch note is too short to carry a punchline")
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as handle:
        handle.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
