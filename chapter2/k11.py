#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import re


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        print(''.join([re.sub(r'\t', ' ', x) for x in fin]))

if __name__ == '__main__':
    main()
