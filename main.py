"""Entry for make.fun bounty u-xvader-tell-a-whole-story-in-32-characters-f86dd978.

Writes a single Wi-Fi network name of at most 32 characters to
/output/entry.txt: the funniest name that hints at a whole story,
as seen in a phone's network list.
"""

ENTRY = "ITookTheKidsAndTheWiFi"


def main() -> None:
    """Validate the entry name and write it to /output/entry.txt."""
    import os

    if not isinstance(ENTRY, str):
        raise ValueError("entry must be a string")
    if not ENTRY.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in ENTRY or "\r" in ENTRY:
        raise ValueError("entry must be a single line")
    if len(ENTRY) < 1 or len(ENTRY) > 32:
        raise ValueError("entry must be 1 to 32 characters")

    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
