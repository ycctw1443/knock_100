#!/usr/bin/env python
# -- coding:utf-8 -*-
from collections import Counter
try:
    import cPickle as pickle
except:
    import pickle


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    word_list = []
    for words in m_list:
        str_list = [dic['surface'] for dic in words]
        word_list.extend(str_list)
    count = Counter(word_list)
    for k, v in count.most_common():
        print(k, v)

if __name__ == '__main__':
    main()
