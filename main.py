"""Make the AI Judge Feel Nostalgic entry: a childhood memory.

Writes the entry line to /output/entry.txt. Standard library only.
The line must stay a single sentence: one concrete image, one wry
last beat — nostalgia the judge can picture, not generic sentiment.
"""

import os

ENTRY = (
    "My childhood VHS rental is three days overdue, and somewhere a "
    "video store clerk is still waiting for his rewind fee."
)


def main():
    # Contract: one nostalgic line, under 200 characters.
    assert 30 <= len(ENTRY) < 200, f"entry length {len(ENTRY)} out of band"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(ENTRY)


if __name__ == "__main__":
    main()
