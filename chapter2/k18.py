#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        input_list = [line for line in fin]
        sorted_list = sorted(input_list, key=lambda x: x.split('\t')[2])
        print(''.join([line for line in sorted_list]))

if __name__ == '__main__':
    main()
