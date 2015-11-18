#!/usr/bin/env python
#-- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle

def main():
    list = pickle.load(open('neko.txt.mecab.pkl','rb'))
    for words in list:
        for i in range(1,len(words)):
            if words[i]['surface'] == u'の' and words[i-1]['pos'] == u'名詞' and words[i+1]['pos'] == u'名詞':
                print(words[i-1]['surface'] + u'の' + words[i+1]['surface'])
if __name__ == '__main__':
    main()
