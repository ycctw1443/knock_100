#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    for words in m_list:
        print(' '.join([d['base'] for d in words if d['pos'] == u'動詞']))

if __name__ == '__main__':
    main()
