from main import functions


word = "h[e~llo"
word2 = "don't"


def test_scrub():
    assert "\'" not in functions.scrub(word2)
    assert "[" not in functions.scrub(word)
    assert "~" not in functions.scrub(word)
