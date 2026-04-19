from batompreto.text_filters import normalize_chat_text, text_similarity


def test_normalize_chat_text():
    assert normalize_chat_text("Hi!!!   there...") == "Hi! there."


def test_text_similarity_identical():
    assert text_similarity("hello", "hello") == 1.0
