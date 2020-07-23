import numpy as np
import os
import re
from PIL import Image
from os import path
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import json
from helpers import getList

current_folder = os.path.dirname(os.path.abspath(__file__))
config = ""
with open(current_folder+'/config.json') as f:
    config = json.load(f)


def makeImage(list_words):
    cloud_mask = np.array(Image.open("cloud_mask.png"))

    wc = WordCloud(background_color="white", max_words=2000,
                   mask=cloud_mask, contour_width=3,
                   contour_color='steelblue')
    # generate word cloud
    list_remove = config['ignoreWords']
    dict_words = {}

    for words in list_words:
        if words.word not in list_remove and words.count >= config[
         'minimOccurrences']:
            dict_words.update({words.word: words.count})

    wc.generate_from_frequencies(dict_words)

    # show
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.figure()
    plt.imshow(cloud_mask, cmap=plt.cm.gray, interpolation='bilinear')
    plt.axis("off")
    wc.to_file(path.join(d, "cloud_out.png"))
    plt.show()


# get data directory (using getcwd() is needed to support running example in
# generated IPython notebook)
d = path.dirname(__file__) if "__file__" in locals() else os.getcwd()

fileText = open(config['file'].replace("\\", " / "), "r")
list_words = getList(fileText.readlines())
fileText.close()

makeImage(list_words)
