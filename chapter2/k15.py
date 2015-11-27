#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    num = int(input())
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        input_list = [line for line in fin]
        print(''.join(input_list[len(input_list)-num:]))

if __name__ == '__main__':
    main()
