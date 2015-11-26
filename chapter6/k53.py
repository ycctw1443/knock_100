#!/usr/bin/env python
# -- coding:utf-8 -*-
# http://qiita.com/yubessy/items/1869ac2c66f4e76cd6c5 参考サイト
import k51
from stemming.porter2 import stem


def main():
    text = k51.get_words('nlp.txt')
    for word in text:
        print(word + '\t' + stem(word))

if __name__ == '__main__':
    main()
