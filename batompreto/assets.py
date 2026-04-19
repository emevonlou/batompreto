import json
from pathlib import Path


def load_quick_phrases(path="data/frases_rapidas_bilingues.json") -> dict:
    file = Path(path)

    if not file.exists():
        return {}

    with file.open("r", encoding="utf-8") as f:
        return json.load(f)
