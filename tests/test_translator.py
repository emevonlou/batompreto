from batompreto.translator import translate_text


def test_translate_text_exists():
    assert callable(translate_text)
