#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def check(dic):
    return True if dic['pos'] == u'名詞' and dic['pos1'] == u'サ変接続' else False


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    print(' '.join(doc['base'] for words in m_list
                   for doc in words if check(doc)))

if __name__ == '__main__':
    main()
