from batompreto.assets import load_quick_phrases


def test_load_quick_phrases_returns_dict():
    data = load_quick_phrases()
    assert isinstance(data, dict)


def test_quick_phrases_has_expected_categories():
    data = load_quick_phrases()
    assert "cumprimentos" in data
    assert "emergencia" in data
    assert "reacoes_rapidas" in data
    assert "despedidas" in data


def test_quick_phrases_categories_are_lists():
    data = load_quick_phrases()
    assert isinstance(data["cumprimentos"], list)
    assert isinstance(data["emergencia"], list)
    assert isinstance(data["reacoes_rapidas"], list)
    assert isinstance(data["despedidas"], list)


def test_quick_phrases_items_have_pt_and_en():
    data = load_quick_phrases()

    for categoria, frases in data.items():
        assert isinstance(frases, list)

        for frase in frases:
            assert "pt" in frase
            assert "en" in frase
            assert isinstance(frase["pt"], str)
            assert isinstance(frase["en"], str)
            assert frase["pt"].strip() != ""
            assert frase["en"].strip() != ""
