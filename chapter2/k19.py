#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
from collections import Counter


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        i_list = [[item for item in line.split('\t')] for line in fin]
        count = Counter([item[0] for item in i_list])
        sorted_list = sorted(i_list, key=lambda x: count[x[0]], reverse=True)
        print(''.join('\t'.join(line) for line in sorted_list))

if __name__ == '__main__':
    main()
