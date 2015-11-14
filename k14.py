#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs

def main():
    num = int(input())
    with codecs.open('hightemp.txt','r','utf-8') as fin:
        print(''.join([line for line in fin][:num]))

if __name__ == '__main__':
    main()
