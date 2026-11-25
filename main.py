#!/usr/bin/env python3
"""The Best Meal You Ever Had - make.fun entry (program/v1).

Prints one line about the best meal ever had and writes that same line
to /output/entry.txt (1-200 characters, UTF-8), for the sealed gate.
"""

import os

LINE = (
    "My grandmother's rendang, eaten with bare hands off a banana leaf "
    "at dusk, steam fogging my glasses as the beef fell apart before "
    "I could chew."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
