#!/usr/bin/env python
# -- coding:utf-8 -*-
from collections import Counter
try:
    import cPickle as pickle
except:
    import pickle
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    word_list = []
    for words in m_list:
        str_list = [dic['surface'] for dic in words]
        word_list.extend(str_list)
    ranking = Counter(word_list).most_common(10)

    fontpath = '/System/Library/Fonts/ヒラギノ角ゴ ProN W3.otf'
    fp = FontProperties(fname=fontpath)
    plt.bar(np.arange(10), [v for k, v in ranking], align='center')
    plt.xticks(np.arange(10), [k for k, v in ranking], fontproperties=fp)
    plt.show()

if __name__ == '__main__':
    main()
