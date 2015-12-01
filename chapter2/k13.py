#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


def main():
    with codecs.open('col1.txt', 'r', 'utf-8') as fin:
        list1 = [line.strip() for line in fin]
    with codecs.open('col2.txt', 'r', 'utf-8') as fin:
        list2 = [line.strip() for line in fin]
    with codecs.open('output13.txt', 'w', 'utf-8') as fout:
        fout.write('\n'.join(s1+'\t'+s2 for (s1, s2) in zip(list1, list2)))

if __name__ == '__main__':
    main()
