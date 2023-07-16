# QIUHE WANG
Words = input("")

ListOfWords = Words.split()

wordsFreq = {}


for i in range(0, len(ListOfWords)):
    word = ListOfWords[i]
    if word not in wordsFreq:
        wordsFreq[word] = 1
    else:  # Otherwise
        wordsFreq[word] = wordsFreq[word] + 1


for i in range(0, len(ListOfWords)):
    print(ListOfWords[i], wordsFreq[ListOfWords[i]])  