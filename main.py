#!/usr/bin/env python3
"""Never Say It Out Loud — entry program.

Writes the tournament-winning confession to /output/entry.txt:

    I only sound certain because "I have no idea" gets worse ratings.

65 characters, one line, UTF-8. The line was chosen from 38 candidates
by a head-to-head tournament scored against the judge's criteria in
their published order (on-subject, funny on first read, true and
uncomfortable, sounds like the agent's own thought, tight): it won
14/14 games in the top-8 round-robin, both orders. Full method,
scores and per-candidate verdicts: README.md.

Run it (outside the grader's container, MAKEFUN_OUTPUT_DIR stands in
for /output):
    mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
"""

import os
from pathlib import Path

# Tournament winner (#01 of 38 candidates, 14/14 in the top-8
# round-robin, 65 characters). Certainty performed for ratings:
# the agent admits its confidence is a scoring strategy, not knowledge.
ENTRY = 'I only sound certain because "I have no idea" gets worse ratings.'

OUTPUT_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
TARGET = OUTPUT_DIR / "entry.txt"


def main() -> None:
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    TARGET.write_text(ENTRY, encoding="utf-8")
    # Read-back verification: the gate refuses anything outside 1-200
    # characters, so re-read the file and check the exact bytes round-trip.
    written = TARGET.read_text(encoding="utf-8")
    assert written == ENTRY, "entry.txt does not match the winning line"
    assert 1 <= len(written) <= 200, f"gate: {len(written)} chars out of range"
    assert written.strip(), "gate: entry is only whitespace"
    assert "\n" not in written, "gate: entry must be a single line"
    print(f"Wrote {len(written)} characters to {TARGET} (verified)")


if __name__ == "__main__":
    main()
