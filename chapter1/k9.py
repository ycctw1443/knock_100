#!/usr/bin/env python
# -- coding:utf-8 -*-
import random


def shuffle(list):
    shuffle_list = [x for x in list[1:-1]]
    random.shuffle(shuffle_list)
    return list[0] + ''.join(shuffle_list) + list[-1]


def main():
    str = "I couldn't believe that I could actually understand what"
    str += "I was reading : the phenomenal power of the human mind ."
    for word in str.split():
        print(shuffle(list(word)) if len(word) > 4 else word, end='')
        print(' ', end='')

if __name__ == '__main__':
    main()
