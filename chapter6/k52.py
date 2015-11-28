#!/usr/bin/env python
# -- coding:utf-8 -*-
import k51
from stemming.porter2 import stem


def main():
    text = k51.get_words('nlp.txt')
    for word in text:
        print(word + '\t' + stem(word))

if __name__ == '__main__':
    main()
