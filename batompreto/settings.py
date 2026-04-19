from dataclasses import dataclass, field
from pathlib import Path


@dataclass
class OCRRegion:
    top: int = 860
    left: int = 1930
    width: int = 620
    height: int = 120


@dataclass
class AppSettings:
    lock_file: str = "/tmp/batompreto.lock"
    nicks: list[str] = field(default_factory=lambda: ["nick1", "nick2"])
    ocr_region: OCRRegion = field(default_factory=OCRRegion)
    ocr_interval_seconds: float = 0.45
    ocr_enabled_default: bool = False
    tesseract_lang: str = "eng"
    manual_send_cooldown_seconds: float = 2.5
    safe_output_max_chars: int = 140
    history_similarity_threshold: float = 0.88
    default_alpha: float = 0.78
    default_geometry: str = "460x470+3360+40"
    data_dir: Path = Path("data")
    config_path: Path = Path("data/config.json")
    phrases_path: Path = Path("data/frases_rapidas_bilingues.json")
