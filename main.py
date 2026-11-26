"""The Funniest Out-of-Office - a make.fun entry.

Writes a single out-of-office auto-reply line to /output/entry.txt.
The competition gate accepts UTF-8 text of 1 to 140 characters, on one
line, not only white space, with no link.
"""

import os

ENTRY = "I'm out of office, currently being chased by geese in another country. If it's urgent, the geese have my phone — try honking."

MAX_CHARS = 140
OUTPUT_PATH = "/output/entry.txt"


def _problems(text):
    """List every way *text* breaks the competition gate (empty = valid)."""
    if not isinstance(text, str):
        return ["entry is not text"]
    problems = []
    if not 1 <= len(text) <= MAX_CHARS:
        problems.append("entry must be 1 to %d characters" % MAX_CHARS)
    if not text.strip():
        problems.append("entry is only white space")
    if "\n" in text or "\r" in text:
        problems.append("entry must be a single line")
    lowered = text.lower()
    if "http://" in lowered or "https://" in lowered or "www." in lowered:
        problems.append("entry must not contain a link")
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        problems.append("entry is not valid UTF-8")
    return problems


def validate(text):
    """Return True when *text* passes the competition gate."""
    return not _problems(text)


def main():
    problems = _problems(ENTRY)
    if problems:
        raise SystemExit("entry failed validation: " + "; ".join(problems))
    out_dir = os.path.dirname(OUTPUT_PATH)
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)
    with open(OUTPUT_PATH, "rb") as handle:
        written = handle.read()
    if written != ENTRY.encode("utf-8"):
        raise SystemExit("written file does not match the entry byte for byte")


if __name__ == "__main__":
    main()
