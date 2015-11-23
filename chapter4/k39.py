#!/usr/bin/env python
# -- coding:utf-8 -*-
from collections import Counter
try:
    import cPickle as pickle
except:
    import pickle
import numpy as np
import matplotlib.pyplot as plt


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    word_list = []
    for words in m_list:
        str_list = [dic['surface'] for dic in words]
        word_list.extend(str_list)
    ranking = Counter(word_list).most_common()

    plt.xscale('log')
    plt.yscale('log')
    plt.scatter(np.arange(len(ranking)) + 1, [v for k, v in ranking])
    # こっちでも同じ結果になる
    # plt.loglog(np.arange(len(ranking)) + 1, [v for k, v in ranking], 'o')
    plt.show()

if __name__ == '__main__':
    main()
