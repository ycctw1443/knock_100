#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def check(i, word):
    if word[i]['surface'] == u'の' and word[i-1]['pos'] == u'名詞':
        if word[i+1]['pos'] == u'名詞':
            return True
    return False


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    print('\n'.join(word[i-1]['surface'] + u'の' + word[i+1]['surface']
                    for word in m_list for i in range(1, len(word)-1)
                    if check(i, word)))

if __name__ == '__main__':
    main()
