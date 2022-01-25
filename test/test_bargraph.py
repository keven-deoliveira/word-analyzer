import matplotlib.pyplot as plt


def barGraph(wordcount):
    plt.figure(dpi=50)
    plt.bar(wordcount.keys(), wordcount.values(), width=0.5, edgecolor='black', color='#ADD8E6')
    plt.xticks(rotation=90)
    plt.xlabel("Word", fontweight='bold')
    plt.ylabel("Count", fontweight='bold')
    plt.show()


wordcount = {"hello": 4, "test": 2, "color": 6, "histogram": 1, "software": 11}


def test_histogram():
    assert barGraph(wordcount) is None  #should not return anything
