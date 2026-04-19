import json
from pathlib import Path


def load_nicks(config_path: str | Path) -> list[str]:
    path = Path(config_path)

    if not path.exists():
        return []

    with path.open("r", encoding="utf-8") as f:
        data = json.load(f)

    return data.get("nicks", [])


def save_nicks(config_path: str | Path, nicks: list[str]) -> None:
    path = Path(config_path)
    data = {}

    if path.exists():
        with path.open("r", encoding="utf-8") as f:
            data = json.load(f)

    data["nicks"] = nicks

    with path.open("w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
