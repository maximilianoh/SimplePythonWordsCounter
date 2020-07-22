import re


class WordClass:
    def __init__(self, name):
        self.word = name
        self.count = 1

    def add_count(self):
        self.count += 1

    def __lt__(self, other):
        if int(self.count) == int(other.count):
            return self.word < other.word
        return int(self.count) > int(other.count)

    def __repr__(self):
        return '{}: {} {}'.format(self.__class__.__name__, self.word,
                                  self.count)


def cleanWord(word, list_words):
    boolean = False
    for objects in list_words:
        if objects.word == word:
            objects.add_count()
            boolean = True

    if not boolean:
        w = WordClass(word)
        list_words.append(w)


def getList(lines):
    list_words = []
    for linea in lines:
        if linea.strip():
            list_result = linea.split(" ")
            for word_split in list_result:
                word = re.sub(r'[…“,.()\[\]":»«-¿?]', "",
                              word_split.upper().strip())
                if word.strip():
                    cleanWord(word, list_words)

    list_words.sort()
    return list_words
