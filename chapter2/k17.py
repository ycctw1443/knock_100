#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        input_list = [[item for item in line.split('\t')] for line in fin]
        print('\n'.join(set([item[0] for item in input_list])))

if __name__ == '__main__':
    main()
