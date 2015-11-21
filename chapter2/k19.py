#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
from collections import Counter


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        list = [[x for x in line.split('\t')] for line in fin]
        count = Counter([x[0] for x in list])
        sorted_list = sorted(list, key=lambda x: count[x[0]], reverse=True)
        print(''.join(['\t'.join(line) for line in sorted_list]))

if __name__ == '__main__':
    main()
