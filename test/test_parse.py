def parse(document):
    wordcount = {}

    # with NLTK, might have to replace ' with a space or something
    NLTK = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself", "yourselves", "he", "him", "his", 
    "himself", "she", "her", "hers", "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which", 
    "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", 
    "having", "do", "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", 
    "for", "with", "about", "against", "between", "into", "through", "during", "before", "after", "above", "below", "to", "from", "up", 
    "down", "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "here", "there", "when", "where", "why", "how", 
    "all", "any", "both", "each", "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", 
    "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    for word in document.split():
        if "'" in word:
            word = word.replace("'", " ")

        word_split = word.split()  # words with apostrophe separated by whitespace, now put into indexable structure to check NLTK
        
        if word_split[0] in NLTK:
            continue
        elif word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    return wordcount


test_str = "hello hello\nhello test test\ntest me me me me me again don't"


def test_parse():
    wordcount = parse(test_str)
    assert wordcount is not None  # should not be empty / should return something
    assert isinstance(wordcount, dict)  # should return a dictionary
    assert "me" not in wordcount  # NLTK words should not be in dictionary
    assert "again" not in wordcount  # NLTK words should not be in dictionary
    assert "don't" not in wordcount  # NLTK word checking, this time with apostrophes
