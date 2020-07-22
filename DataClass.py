from collections import defaultdict

listSentence = []
dictData = dict()
class Autocompete:
    def __init(self, completed_sentence, source_text,offset, score):
        self.__completed_sentence = completed_sentence
        self.__source_text =source_text
        self.__offset = offset
        self.__score = score


#def read_file(filename):
with open("about.txt") as file:
    listSentence = file.read().split("\n")


def init_data():
    for i in range(len(listSentence)):
        for j in range(len(listSentence[i])):
            dictData.setdefault((listSentence[i])[:j+1], set()).add(i)
        listWords = listSentence[i].split(" ")
        for k in range(len(listWords)):
            for j in range(len(listWords[k])+1):
                dictData.setdefault((listWords[k])[:j+1], set()).add(i)


def fix(word, count):
   listSentenceBast = []
#   for i in count:
#      for char in range(ord('a'), ord('z') + 1):
#          if dictData.get(char + word):
#              for j in range(len(dictData[char + word])):
#                  listSentenceBast.append((dictData[char + word])[j])

#def replace_str(word, count):
#    listSentencesBast = []
#    for i in range(count):
#        for char in range(ord('a'), ord('z')+1):
#            for j in range(len(word)):
#                if dict.get(word[:j]+char+word[j+1:]):
#                    for k in range(len(word[:j]+char+word[j+1:])):
#                        listSentencesBast.append((dict[word[:j]+char+word[j+1:]])[k])
#    print(listSentencesBast)


def get_best_k_comyhetion(word):
    listSentenceBast = []
    if dictData.get(word):
        for i in list(dictData[word]):
            listSentenceBast.append(listSentence[i])
        listSentenceBast.sort()
        if len(listSentenceBast) >= 5:
            return (listSentenceBast[:5])
        else:
            listSentenceBast.append(fix(word, 5-len(listSentenceBast)))
    else:
        listSentenceBast.append(fix(word, 5))
    return (listSentenceBast.sort())



#read_file("abc.txt")
init_data()
print(dictData)

list = get_best_k_comyhetion("the")
#replace_str("am", 2)
print(list)