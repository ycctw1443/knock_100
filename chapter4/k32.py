#!/usr/bin/env python
#-- coding:utf-8 -*-
import cPickle as pickle

def main():
    list = pickle.load(open('neko.txt.mecab.pkl','rb'))
    for words in list:
        print(','.join([dic['base'] for dic in words if dic['pos'] == u'動詞']))

if __name__ == '__main__':
    main()
