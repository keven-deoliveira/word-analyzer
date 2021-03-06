import matplotlib.pyplot as plt
from string import punctuation


# scrubs word for special characters, removes them
def scrub(word):
    copy = word
    special_chars = list(punctuation)

    for char in copy:
        if char in special_chars:
            copy = copy.replace(char, "")

    return copy


# checks if word is in the NLTK list, returns True if yes
def checkNLTK(word):
    NLTK = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours",
            "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself",
            "it", "its", "itself", "they", "them", "their", "theirs", "themselves", "what", "which",
            "who", "whom", "this", "that", "these", "those", "am", "is", "are", "was", "were", "be",
            "been", "being", "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
            "the", "and", "but", "if", "or", "because", "as", "until", "while", "of", "at", "by", "for",
            "with", "about", "against", "between", "into", "through", "during", "before", "after", "above",
            "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again", "further",
            "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each", "few",
            "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
            "very", "s", "t", "can", "will", "just", "don", "should", "now"]

    if "'" in word:
        word = word.replace("'", " ")

    word_split = word.split()

    if any(x in word_split for x in NLTK):
        return True

    return False


# parse document (string), return dictionary of words and their count
def parse(document):
    wordcount = {}

    for word in document.split():
        if checkNLTK(word):
            continue
        elif word not in wordcount:
            word = scrub(word)
            wordcount[word] = 1
        else:
            word = scrub(word)
            wordcount[word] += 1

    return wordcount


# takes dictionary as input and creates histogram // working on this still
def barGraph(wordcount):
    plt.figure(dpi=80)
    plt.bar(wordcount.keys(), wordcount.values(), width=0.5, edgecolor='black', color='#ADD8E6')
    plt.xticks(rotation=90)
    plt.xlabel("Word", fontweight='bold')
    plt.ylabel("Count", fontweight='bold')
    plt.show()
