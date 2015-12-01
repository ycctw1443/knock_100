#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        list = [[item for item in line.split('\t')] for line in fin]
    with codecs.open('col1.txt', 'w', 'utf-8') as fout:
        fout.write('\n'.join(x[0] for x in list))
    with codecs.open('col2.txt', 'w', 'utf-8') as fout:
        fout.write('\n'.join(x[1] for x in list))

if __name__ == '__main__':
    main()
