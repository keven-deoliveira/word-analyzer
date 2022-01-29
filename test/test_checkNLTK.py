from main import functions


def test_checkNLTK():
    assert functions.checkNLTK("i") is True
    assert functions.checkNLTK("how") is True
    assert functions.checkNLTK("don't") is True
    assert functions.checkNLTK("can") is True
    assert functions.checkNLTK("can't") is True
    assert functions.checkNLTK("omegalol") is False
