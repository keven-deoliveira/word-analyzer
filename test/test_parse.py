def parse(document):
    wordcount = {}
    for word in document.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    return wordcount


test_str = "hello hello hello\nhello testing test test\ntest\ntest me me me me me again"


def test_parse():
    assert parse(test_str) is not None  # should not be empty / should return something
    assert isinstance(parse(test_str), dict)  # should return a dictionary
    assert ("me" not in parse(test_str)) and ("again" not in parse(test_str))  # NLTK works should not be in dictionary
