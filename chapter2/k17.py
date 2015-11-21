#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        list = [[x for x in line.split('\t')] for line in fin]
        print('\n'.join(set([x[0] for x in list])))

if __name__ == '__main__':
    main()
