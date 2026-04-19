import re
from difflib import SequenceMatcher


def normalize_chat_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = re.sub(r"[!?]{2,}", "!", text)
    text = re.sub(r"\.{2,}", ".", text)
    text = re.sub(r"([,;:]){2,}", r"\1", text)
    return text


def text_similarity(a: str, b: str) -> float:
    return SequenceMatcher(None, a.lower(), b.lower()).ratio()


def prepare_text_for_chat(text: str, max_chars: int) -> tuple[str | None, str | None]:
    text = normalize_chat_text(text)

    if len(text) < 2:
        return None, "Text too short."

    if len(text) > max_chars:
        text = text[:max_chars].rstrip()

    return text, None


def clean_ocr_text(text: str) -> str:
    blocked = [
        "while",
        "true",
        "hacknet",
        "arraste",
        "duas vezes",
        "auto ocr",
        "copy",
        "clear",
        "input",
        "output",
        "batompreto",
        "www.hypixel.net",
        "skyblock",
        "bed wars",
        "duels",
        "coins",
        "lobby",
        "prototype",
        "click here",
        "right click",
    ]

    lines = []
    for line in text.splitlines():
        line = line.strip()

        if not line or len(line) < 3:
            continue

        if all(ch in "-_=|/\\[](){}<>.:;,'`~" for ch in line):
            continue

        if any(word in line.lower() for word in blocked):
            continue

        lines.append(line)

    return "\n".join(lines[-2:]).strip()
