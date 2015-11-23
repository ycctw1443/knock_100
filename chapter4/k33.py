#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def check(dic):
    if dic['pos'] == u'名詞' and dic['pos1'] == u'サ変接続':
        return True
    else:
        return False


def main():
    list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    for words in list:
        print(' '.join([d['base'] for d in words if check(d)]))

if __name__ == '__main__':
    main()
