#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs

def main():
    with codecs.open('hightemp.txt','r','utf-8') as fin:
        print(sum(1 for line in fin))

if __name__ == '__main__':
    main()
