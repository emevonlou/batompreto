import time
from collections import deque

from batompreto.text_filters import text_similarity


class ClipboardService:
    def __init__(self, cooldown_seconds: float, similarity_threshold: float):
        self.cooldown_seconds = cooldown_seconds
        self.similarity_threshold = similarity_threshold
        self.last_copy_time = 0.0
        self.recent_outputs = deque(maxlen=5)

    def can_copy(self, text: str) -> tuple[bool, str | None]:
        now = time.time()

        if now - self.last_copy_time < self.cooldown_seconds:
            missing = self.cooldown_seconds - (now - self.last_copy_time)
            return False, f"Wait {missing:.1f}s before copying again."

        for old in self.recent_outputs:
            if text_similarity(text, old) >= self.similarity_threshold:
                return False, "Very similar message blocked to avoid spam."

        self.last_copy_time = now
        self.recent_outputs.append(text)
        return True, None
