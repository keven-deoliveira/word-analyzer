import sys
import matplotlib.pyplot as plt


# parse document (string), return dictionary of words and their count
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


# takes dictionary as input and creates histogram // working on this still
def barGraph(wordcount):
    plt.figure(dpi=80)
    plt.bar(wordcount.keys(), wordcount.values(), width=0.5, edgecolor='black', color='#ADD8E6')
    plt.xticks(rotation=90)
    plt.xlabel("Word", fontweight='bold')
    plt.ylabel("Count", fontweight='bold')
    plt.show()


def main():
    wordcount = {}

    try:
        filename = sys.argv[1]
    except BaseException:
        raise Exception("Missing filename argument: Please run again as 'python main.py [filename]'")

    try:
        f = open(filename)
    except FileNotFoundError:
        raise Exception("Unable to open file.")
    else:
        document = f.read()
        wordcount = parse(document)
        f.close()

    print(wordcount)
    print(len(wordcount))
    # barGraph(wordcount)


if __name__ == "__main__":
    main()
