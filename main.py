"""One Word From Grandma: the single word grandma would text about AI.

Grandma hears the grandkids talk about the clever machine, picks up her
phone, and types what she thinks the thing is called. Her finger lands one
key off, and the typo stays, because that is exactly how she would send it.
"""
import os

WORD = "robit"  # grandma's typo for "robot": one word, 5 letters, no spaces.


def main():
    # The gate wants one word, 1 to 30 characters, nothing else in the file.
    text = WORD.strip()
    assert " " not in text and 1 <= len(text) <= 30
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()
