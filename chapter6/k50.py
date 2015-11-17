#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import re

def main():
    with codecs.open('nlp.txt','r','utf-8') as fin:
        text = ''.join([re.sub(r'\n','',line) for line in fin])
        print('\n'.join([str for str in re.sub(r'([.;:?!])\s([A-Z])',r'\1\n\2',text).split('\n')]))

if __name__ == '__main__':
    main()
