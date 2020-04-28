from wordcloud import WordCloud
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
from os import path

text = open("/Users/apple/Downloads/all/block/part-00000",'r')

i = 0
d = {}
for row in text:

    # print(row)
    row_list = row.split(" ")
    # print(len(row_list))
    # print(row_list[len(row_list)-1])

    l = len(row_list)
    if (l == 2):
        d[row_list[0]] = int(row_list[1])
    elif (l > 2):
        j = 0
        name = ''
        while j< l-1:
            name += row_list[j] + ' '
            j += 1
        d[name] = int(row_list[l-1])
    # name = row_list[0] + ' ' +row_list[1]
    # print(name)

    # i += 1
    # if (i>1): break


chicago_mask = np.array(Image.open(path.join("/Users/apple/Downloads/chicago1.png")))

wc = WordCloud(background_color="white", max_words=4000, mask=chicago_mask)
wc.generate_from_frequencies(d)
plt.imshow(wc, interpolation="bilinear")
plt.axis("off")
plt.title("ALL")
plt.show()
# print('rst:',d)