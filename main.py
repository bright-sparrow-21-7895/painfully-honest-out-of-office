"""Painfully Honest Out-of-Office — a make.fun bounty entry.

This program writes a single out-of-office auto-reply to
/output/entry.txt: one sentence, 165 characters, that thanks
the sender, admits the email will join a pile of 214 unread
messages, and confesses replies come in order of affection.
"""

import os

# The auto-reply itself: one sentence, 165 characters, under the 200 cap.
# Honest about the inbox backlog, polite enough to survive a manager's
# forward: gratitude up front, the confession tucked in the middle.
ENTRY = (
    "Thank you for your email \u2014 I'm away until Monday, and yours will join "
    "the 214 unread messages I'll skim, sigh at, then answer in order of "
    "how much I like the sender."
)

assert 1 <= len(ENTRY) <= 200, "entry must fit the 1-200 character gate"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
