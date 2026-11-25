"""The Word You'd Delete From the Dictionary.

Entry: queue — q followed by four silent letters standing in line.
Delete it and nothing is lost, because those four letters never did
any work in the first place.
"""

import os

WORD = "queue"


def main():
    # Self-gate mirroring the sealed scorer: UTF-8, 1-77 chars, one word.
    assert 1 <= len(WORD) <= 77
    assert WORD.strip() == WORD and WORD.strip()
    assert len(WORD.split()) == 1 and "\n" not in WORD
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.dirname(
        os.path.abspath(__file__)
    )
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(WORD + "\n")
    print(WORD)


if __name__ == "__main__":
    main()
