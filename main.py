"""Write the thankful entry text to /output/entry.txt.

Stdlib only. Deterministic: the same bytes on every run.
No trailing newline; the text is exactly 348 Unicode code points.
"""

import os

TEXT = (
    "She keeps it in the book she reads from every spring:\n"
    "a dandelion, pressed flat years ago\n"
    "by a small hand that could not yet write its name.\n"
    "The yellow has gone the colour of old paper.\n"
    "The stem is thin as thread.\n"
    "She turns to that page, and it is still there.\n"
    "Some thank-yous are never said.\n"
    "They are kept.\n"
    "Thank you for keeping this one with her."
)

EXPECTED_CODE_POINTS = 348
EXPECTED_BYTES = 348


def main() -> None:
    assert 1 <= len(TEXT) <= 1000, "entry must be 1-1000 code points"
    assert len(TEXT) == EXPECTED_CODE_POINTS, (
        f"expected {EXPECTED_CODE_POINTS} code points, got {len(TEXT)}"
    )
    assert TEXT == TEXT.strip(), "no leading or trailing whitespace"
    assert TEXT.isascii(), "entry is plain ASCII"
    data = TEXT.encode("utf-8")
    assert len(data) == EXPECTED_BYTES, (
        f"expected {EXPECTED_BYTES} bytes, got {len(data)}"
    )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "wb") as f:
        f.write(data)
    # Read-back verification: confirm what was written is exactly TEXT.
    with open("/output/entry.txt", "rb") as f:
        written = f.read()
    assert written == data, "read-back bytes differ from TEXT"
    assert len(written.decode("utf-8")) == EXPECTED_CODE_POINTS, (
        "read-back is not 348 code points"
    )


if __name__ == "__main__":
    main()
