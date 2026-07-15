import re


def _parse(text: str) -> list[str]:
    return [
        re.sub(r"^\d+[\.\)]\s*", "", line).strip()
        for line in text.splitlines()
        if line.strip()
    ]


def test_parses_numbered_list():
    raw = "1. Tell me about yourself\n2) Why this role?\n3. Describe a challenge"
    parsed = _parse(raw)
    assert parsed == ["Tell me about yourself", "Why this role?", "Describe a challenge"]


def test_ignores_blank_lines():
    raw = "1. First\n\n2. Second\n\n"
    parsed = _parse(raw)
    assert parsed == ["First", "Second"]
