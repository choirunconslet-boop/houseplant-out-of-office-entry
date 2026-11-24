"""The Houseplant Out-of-Office — make.fun bounty entry.

Writes one funny out-of-office auto-reply, as if a houseplant sent it,
to /output/entry.txt. Pure stdlib; no network, no secrets.
"""

import os

ENTRY = (
    "Out of office: I'm a fern, unwatered since March. "
    "The cactus and I have unionised. "
    "No water, no reply."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 120, f"entry is {len(text)} chars, must be 1-120"
    assert text.strip(), "entry must not be only whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
