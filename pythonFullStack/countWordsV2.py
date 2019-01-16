# countWords.py
import string
import os

bookDir = '../..'
bookPath = os.path.join(bookDir, 'Around the World in 80 Days.txt')
print(bookPath)
with open(bookPath) as f:
    contents = f.read()

stopWords = ['i', 'me', 'my', 'myself', 'we', 'our', 'ours',
             'ourselves', 'you', "you're", "you've", "you'll", "you'd", 'your',
             'yours', 'yourself', 'yourselves', 'he', 'him', 'his', 'himself', 'she',
             "she's", 'her', 'hers', 'herself', 'it', "it's", 'its', 'itself',
             'they', 'them', 'their', 'theirs', 'themselves', 'what', 'which', 'who',
             'whom', 'this', 'that', "that'll", 'these', 'those', 'am', 'is', 'are',
             'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had', 'having',
             'do', 'does', 'did', 'doing', 'a', 'an', 'the', 'and', 'but', 'if',
             'or', 'because', 'as', 'until', 'while', 'of', 'at', 'by', 'for',
             'before', 'after', 'above', 'below', 'to', 'from', 'up', 'down', 'in',
             'out', 'on', 'off', 'over', 'under', 'again', 'further', 'then', 'once',
             'here', 'there', 'when', 'where', 'why', 'how', 'all', 'any', 'both',
             'each', 'few', 'more', 'most', 'other', 'some', 'such', 'no', 'nor',
             'not', 'only', 'own', 'same', 'so', 'than', 'too', 'very', 's', 't',
             'can', 'will', 'just', 'don', "don't", 'should', "should've", 'now',
             'd', 'll', 'm', 'o', 're', 've', 'y', 'ain', 'aren', "aren't", 'couldn',
             "couldn't", 'didn', "didn't", 'doesn', "doesn't", 'hadn', "hadn't",
             'hasn', "hasn't", 'haven', "haven't", 'isn', "isn't", 'ma', 'mightn',
             "mightn't", 'mustn', "mustn't", 'needn', "needn't", 'shan', "shan't",
             'shouldn', "shouldn't", 'wasn', "wasn't", 'weren', "weren't", 'won',
             "won't", 'wouldn', "wouldn't", ' ']


def tidy(contents):
    contents = contents.lower()
    translator = str.maketrans('', '', string.punctuation)
    contentsNoPunct = contents.translate(translator)
    contentsNoPunct = contentsNoPunct.split(" ")
    return contentsNoPunct


'''
def wordCount(contentsNoPunct):
    numOfWords = {}
    for i in range(len(contentsNoPunct)):
        if contentsNoPunct[i] in numOfWords:
            numOfWords[contentsNoPunct[i]] += 1
        else:
            if contentsNoPunct[i] in stopWords:
                continue
            else:
                numOfWords[contentsNoPunct[i]] = 1
        words = list(numOfWords.items())
        # .items() returns a list of tuples
        words.sort(key=lambda tup: tup[1], reverse=True)
        # sort largest to smallest, based on count
        # print the top 11 words, or all of them, whichever is smaller
    return words[: 12]
'''

def wordPairCount(contentsNoPunct):
    pairedWords = {}
    for i in range(len(contentsNoPunct) - 1):
        if contentsNoPunct[i] + ' ' + contentsNoPunct[i + 1] in pairedWords:
            pairedWords[contentsNoPunct[i] + ' ' + contentsNoPunct[i + 1]] += 1
        else:
            if contentsNoPunct[i] in stopWords or contentsNoPunct[i + 1] in stopWords or contentsNoPunct[i] == "" or contentsNoPunct[i + 1] == "":
                continue
            else:
                pairedWords[contentsNoPunct[i] + ' ' + contentsNoPunct[i + 1]] = 1
        words = list(pairedWords.items())
        words.sort(key=lambda tup: tup[1], reverse=True)
    return words[: 10]


# print(wordCount(tidy(contents)))
print(wordPairCount(tidy(contents)))
