#!/usr/bin/env python
# -- coding:utf-8 -*-
import random


def shuffle(char_list):
    shuffle_list = [x for x in char_list[1:-1]]
    random.shuffle(shuffle_list)
    return char_list[0] + ''.join(shuffle_list) + char_list[-1]


def main():
    sentence = '''
    I couldn't believe that I could actually understand what I was \
    reading : the phenomenal power of the human mind .
    '''.strip()
    print(sentence)
    print(' '.join([shuffle(list(word)) if len(word) > 4 else word
                    for word in sentence.split()]))

if __name__ == '__main__':
    main()
