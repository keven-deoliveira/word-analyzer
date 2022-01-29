from main import functions


test_str = "hello hello\nhello test test\ntest me me me me me again don't"


def test_parse():
    wordcount = functions.parse(test_str)
    assert wordcount is not None  # should not be empty / should return something
    assert isinstance(wordcount, dict)  # should return a dictionary
    assert "me" not in wordcount  # NLTK words should not be in dictionary
    assert "again" not in wordcount  # NLTK words should not be in dictionary
    assert "don't" not in wordcount  # NLTK word checking, this time with apostrophes
