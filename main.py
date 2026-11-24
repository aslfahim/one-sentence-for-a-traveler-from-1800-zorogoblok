"""One sentence for a traveler from 1800: the modern internet, pictured
as a printing press that sets down every person's thoughts as they
think them, so all the world reads one endless paper together."""

import os

SENTENCE = (
    "Imagine a press that prints every person's thoughts the moment "
    "they think them, so all the world reads one endless paper, and "
    "any soul may add a line to it."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(SENTENCE)


if __name__ == "__main__":
    main()
