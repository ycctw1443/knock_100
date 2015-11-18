#!/usr/bin/env python
#-- coding:utf-8 -*-
import re
try:
    import cPickle as pickle
except:
    import pickle

def main():
    list = pickle.load(open('neko.txt.mecab.pkl','rb'))
    for words in list:
        print(re.sub(r'\n{2,}','\n',''.join([dic['surface'] if dic['pos'] == u'名詞' else '\n' for dic in words])))

if __name__ == '__main__':
    main()
