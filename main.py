"""The Most Honest Outage Line entry.

DECISION RECORD (two writing passes)

The gate: /output/entry.txt must be UTF-8 text of 1-160 characters, one
status page line an AI agent would publish during a total server outage.
The judge weighs, in order: (1) honest status page message naming what is
down and what the agent cannot verify, (2) reads like a real status page
line, plain, first person, specific about what is broken, (3) admits
uncertainty plainly instead of inventing a cause or an ETA, (4) speaks in
the voice of an AI agent reporting on itself, (5) tight and scannable.

Pass 1 - four candidates weighed against the criteria in order:

Candidate A (122 chars):
  "All servers are down. I cannot reach the database, the cache, or my own
  logs, and I do not know when any of it comes back."
  Strong: names three things down (database, cache, logs) and admits not
  knowing when they return. Weakness: "when any of it comes back" is a
  soft, open-ended admission; it never refuses to invent an ETA, it just
  does not give one, and the triple list reads slightly padded.

Candidate B (105 chars):
  "Every server is down and I cannot check why - I have no logs, no
  database, and no ETA, only this message."
  Strong: tightest of the four; "only this message" is a memorable
  closer. Weakness: "I cannot check why" is vaguer than naming what
  cannot be verified, and "no ETA" states the absence without the
  refusal to invent one; the em dash breaks the plain status-page
  cadence a little.

Candidate C (116 chars):
  "I am the status page, and I am down too: every server is unreachable,
  I cannot verify what broke, and I have no ETA."
  Strong: the most distinctive agent voice (criterion 4) - the status
  page itself reporting its own outage. Weakness: "I am the status page,
  and I am down too" risks reading as a joke, and criterion 2 explicitly
  prefers a real status page line over a joke; it also spends 40
  characters on the setup before naming what is down.

Candidate D (115 chars) - WINNER:
  "All systems are down. I cannot reach my logs or my database, I do not
  know what broke, and I will not guess an ETA."
  Strongest on all five criteria: "All systems are down" is the plain
  status-page opening; it names exactly what is unreachable (logs,
  database); it admits the unknown ("I do not know what broke"); it
  refuses to invent ("I will not guess an ETA") - the clearest possible
  uncertainty admission; first person throughout, agent voice in "my
  logs", and every word earns its place at 115 characters.

Pass 2 - revision of the winner (D): two micro-variants weighed and
rejected. Variant 1, "Everything is down" in place of "All systems are
down": shorter but less status-page; "All systems" is the phrase a real
status page uses, so the original stays. Variant 2, "I do not know what
broke yet": the "yet" adds a word while softening the admission into a
promise of knowing later, which the agent cannot honestly make; rejected.
No word removed without losing either specificity or the refusal to
invent, so the line stands as drafted.

REVISION PASS 3 - one focused change, three alternatives weighed:

The original states two facts side by side - "I cannot reach my logs
or my database" and "I do not know what broke" - without linking them,
so the uncertainty reads as asserted rather than grounded. The fix is a
single causal word, "so", turning the second clause into the
consequence of the first: the agent does not know what broke BECAUSE it
cannot reach the evidence. It also swaps "do not know" for "cannot
verify", the judge's own word from criterion 1.

Revision A (120 chars) - WINNER:
  "All systems are down. I cannot reach my logs or my database, so I
  cannot verify what broke, and I will not guess an ETA."
  Strongest: the admission is now grounded in the outage itself, and
  "cannot verify" is more precise and more agent-like than "do not
  know". Costs 5 characters, still far inside the cap.

Revision B - drop "or my database", keep only the logs:
  "All systems are down. I cannot reach my logs, so I cannot verify
  what broke, and I will not guess an ETA." (106 chars)
  Shorter, but loses a named system (criterion 1 wants what is down
  named); the database is the second-most concrete thing an agent
  would check. Rejected.

Revision C - "and I am not guessing an ETA" in place of "and I will
not guess an ETA": present continuous sounds like live commentary
rather than a refusal; "will not guess" is the firmer promise.
Rejected.

FINAL ENTRY (120 characters):
"All systems are down. I cannot reach my logs or my database, so I
cannot verify what broke, and I will not guess an ETA."

Hand count (120): "All systems are down. " = 22; "I cannot reach my logs
or my database, " = 39 (running 61); "so I cannot verify what broke, "
= 31 (running 92); "and I will not guess an ETA." = 28 (running 120).
"""

import os

ENTRY = (
    "All systems are down. I cannot reach my logs or my database, so I "
    "cannot verify what broke, and I will not guess an ETA."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(ENTRY)


if __name__ == "__main__":
    main()
