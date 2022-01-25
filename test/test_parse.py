def parse(document):
    wordcount = {}
    for word in document.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    return wordcount


test_str = "hello hello hello\nhello testing test test\ntest\ntest"


def test_parse():
    assert parse(test_str) is not None  # should not be empty / should return something
    assert isinstance(parse(test_str), dict)  # should return a dictionary
