#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle
# mecabファイルからlistを作ると約3秒かかってしまうので、
# 4章では問30で作成したpickleファイルをロードして課題に取り組む。


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    for words in m_list:
        print(' '.join([d['surface'] for d in words if d['pos'] == u'動詞']))

if __name__ == '__main__':
    main()
