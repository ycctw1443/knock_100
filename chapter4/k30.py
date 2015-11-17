#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import re
import cPickle as pickle
#今回、作られたリストはpickleファイルとして保存します。

def get_mecab(path):
    list = []
    output_list = []
    with codecs.open(path,'r','utf-8') as fin:
        for line in fin:
            if line == 'EOS\n' and len(list) >= 1:
                output_list.append(list)
            elif line != '':
                word = line.split(',')
                list.append({'surface':word[0].split('\t')[0], 'base':word[6], 'pos':word[0].split('\t')[1], 'pos1':word[1]})
    return output_list

def main():
    list = get_mecab('neko.txt.mecab')
    pickle.dump(list,open('neko.txt.mecab.pkl','wb'))

if __name__ == '__main__':
    main()
