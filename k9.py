#!/usr/bin/env python
#-- coding:utf-8 -*-
import random

def shuffle(list):
    shuffle_list = [x for x in list[1:-1]]
    random.shuffle(shuffle_list)
    return list[0] + ''.join(shuffle_list) + list[-1]

def main():
    str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    print(' '.join([shuffle(list(s)) if len(s) > 4 else s for s in str.split(' ')]))

if __name__ == '__main__':
    main()
