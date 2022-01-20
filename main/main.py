import sys


# parse document (string), return dictionary of words and their count
def parse(document):
    wordcount = {}
    for word in document.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    return wordcount

# takes dictionary as input and creates histogram
def histogram(wordcount):
    pass


def main():
    wordcount = {}
    filename = sys.argv[1]

    with open(filename) as f:
        document = f.read()
        wordcount = parse(document)
        f.close()

    print(wordcount)

if __name__ == "__main__":
    main()
