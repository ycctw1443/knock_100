#!/usr/bin/env python
#-- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle

def main():
    list = pickle.load(open('neko.txt.mecab.pkl','rb'))
    for words in list:
        print(' '.join([dic['base'] for dic in words if dic['pos'] == u'名詞' and dic['pos1'] == u'サ変接続']))

if __name__ == '__main__':
    main()
