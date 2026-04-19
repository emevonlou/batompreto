from batompreto.clipboard_service import ClipboardService


def test_clipboard_service_allows_first_copy():
    service = ClipboardService(cooldown_seconds=2.5, similarity_threshold=0.88)
    allowed, error = service.can_copy("hello")
    assert allowed is True
    assert error is None
