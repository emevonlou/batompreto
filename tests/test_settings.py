from batompreto.settings import AppSettings


def test_settings_defaults():
    settings = AppSettings()
    assert settings.lock_file == "/tmp/batompreto.lock"
    assert settings.tesseract_lang == "eng"
