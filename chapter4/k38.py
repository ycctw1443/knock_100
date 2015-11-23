#!/usr/bin/env python
# -- coding:utf-8 -*-
from collections import Counter
try:
    import cPickle as pickle
except:
    import pickle
import matplotlib.pyplot as plt


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    word_list = []
    for words in m_list:
        str_list = [dic['surface'] for dic in words]
        word_list.extend(str_list)
    ranking = Counter(word_list).most_common()
    plt.hist([v for k, v in ranking], bins=100, range=(0, 9200))
    plt.show()

if __name__ == '__main__':
    main()
