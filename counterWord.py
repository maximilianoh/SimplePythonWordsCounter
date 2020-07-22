import sys
import os
import json
from helpers import getList

current_folder = os.path.dirname(os.path.abspath(__file__))
config = ""
with open(current_folder+'/config.json') as f:
    config = json.load(f)


fileText = open(config['file'].replace("\\", " / "), "r")
list_words = getList(fileText.readlines())
fileText.close()


list_remove = config['ignoreWords']
dict_words = {}

for words in list_words:
    if words.word not in list_remove and words.count >= config[
            'minimOccurrences']:
        dict_words.update({words.word: words.count})


if not config['outputFile']:
    for key, value in dict_words.items():
        print(key + ': ' + value)
else:
    file_save_name = os.path.dirname(fileText.name) + '/' + os.path.basename(
        fileText.name).replace(".", "_out.", 1)
    file_write = open(file_save_name, "w")

    for key, value in dict_words.items():
        file_write.write(key+': ' + str(value) + '\n')

    file_write.close()
