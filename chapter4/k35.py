#!/usr/bin/env python
# -- coding:utf-8 -*-
try:
    import cPickle as pickle
except:
    import pickle


def main():
    m_list = pickle.load(open('neko.txt.mecab.pkl', 'rb'))
    output = []
    w_str = ''
    for words in m_list:
        for dic in words:
            if dic['pos'] == u'名詞':
                w_str += dic['surface']
            elif w_str:
                output.append(w_str)
                w_str = ''
    print(output)

if __name__ == '__main__':
    main()
