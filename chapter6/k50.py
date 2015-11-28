#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import re


def get_text(path):
    output = []
    with codecs.open(path, 'r', 'utf-8') as fin:
        text = ''.join([re.sub(r'\n', '', line) for line in fin])
    for s in re.sub(r'([.;:?!])\s([A-Z])', r'\1\n\2', text).split('\n'):
        output.append(s)
    return output


def main():
    text = get_text('nlp.txt')
    for s in text:
        print(s)

if __name__ == '__main__':
    main()
