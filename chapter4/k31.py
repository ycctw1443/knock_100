#!/usr/bin/env python
#-- coding:utf-8 -*-
import cPickle as pickle
#mecabファイルからlistを作ると約3秒かかってしまい嫌なので、
#4章では問30で作成したpickleファイルをロードして課題に取り組む。

def main():
    list = pickle.load(open('neko.txt.mecab.pkl','rb'))
    for words in list:
        print(','.join([dic['surface'] for dic in words if dic['pos'] == u'動詞']))

if __name__ == '__main__':
    main()
