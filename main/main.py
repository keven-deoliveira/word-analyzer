import sys
import matplotlib.pyplot as plt
from functions import parse, barGraph


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

    if wordcount:
        print(wordcount)
        print(len(wordcount))
        barGraph(wordcount)
    else:
        print("Empty document.")


if __name__ == "__main__":
    main()
