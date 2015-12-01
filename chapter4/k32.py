#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    print(' '.join(doc['base'] for words in m_list
                   for doc in words if doc['pos'] == u'動詞'))

if __name__ == '__main__':
    main()
