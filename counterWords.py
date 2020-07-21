import sys
import os
import re
import json

current_folder = os.path.dirname(os.path.abspath(__file__))
config = ""
with open(current_folder+'/config.json') as f:
    config = json.load(f)


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


def cleanWord(word):
    boolean = False
    for objects in list_words:
        if objects.word == word:
            objects.add_count()
            boolean = True

    if not boolean:
        w = WordClass(word)
        list_words.append(w)


list_words = []
fileText = open(config['file'].replace("\\", "/"), "r")


for linea in fileText.readlines():
    if linea.strip():
        list_result = linea.split(" ")
        for word_split in list_result:
            word = re.sub(r'[,.()":»«-]', "", word_split.upper().strip())
            if word.strip():
                cleanWord(word)


list_remove = config['ignoreWords']
list_words_result = []
list_words.sort()

for words in list_words:
    if words.word not in list_remove and words.count >= config[
            'minimOccurrences']:
        list_words_result.append(words)


if not config['outputFile']:
    for words in list_words_result:
        print(words)
else:
    file_save_name = os.path.dirname(fileText.name) + '/' + os.path.basename(
        fileText.name).replace(".", "_out.", 1)
    file_write = open(file_save_name, "w")

    for words in list_words_result:
        file_write.write(words.word + ': ' + str(words.count) + '\n')

    file_write.close()
