from main import functions


wordcount = {"hello": 4, "test": 2, "color": 6, "histogram": 1, "software": 11}


def test_histogram():
    assert functions.barGraph(wordcount) is None  # should not return anything
