#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
try:
    import cPickle as pickle
except:
    import pickle
# 今回、作られたリストはpickleファイルとして保存します。


def get_mecab(path):
    s_list = []
    output_list = []
    with codecs.open(path, 'r', 'utf-8') as fin:
        for line in fin:
            if line == 'EOS\n':
                if len(s_list) >= 1:
                    output_list.append(s_list)
                    s_list = []
            else:
                word = line.split(',')
                s_list.append({'surface': word[0].split('\t')[0],
                               'base': word[6],
                               'pos': word[0].split('\t')[1],
                               'pos1': word[1]})
    return output_list


def main():
    m_list = get_mecab('neko.txt.mecab')
    pickle.dump(m_list, open('neko.txt.mecab.pkl', 'wb'))

if __name__ == '__main__':
    main()
