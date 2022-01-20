import sys
import matplotlib.pyplot as plt


# parse document (string), return dictionary of words and their count
def parse(document):
    wordcount = {}
    for word in document.split():
        if word not in wordcount:
            wordcount[word] = 1
        else:
            wordcount[word] += 1

    return wordcount


# takes dictionary as input and creates histogram // working on this still
def histogram(wordcount):
    plt.figure(dpi=50)
    plt.bar(wordcount.keys(), wordcount.values(), width=0.5, edgecolor='black', color='#ADD8E6')
    plt.xticks(rotation=90)
    plt.xlabel("Word", fontweight='bold')
    plt.ylabel("Count", fontweight='bold')
    plt.show()


def main():
    wordcount = {}

    try:
        filename = sys.argv[1]
    except:
        raise Exception("Missing filename argument: Please run again as 'python main.py [filename]'")

    try:
        f = open(filename)
    except:
        raise Exception("Unable to open file.")
    else:
        document = f.read()
        wordcount = parse(document)
        f.close()

    print(len(wordcount))
    histogram(wordcount)


if __name__ == "__main__":
    main()
