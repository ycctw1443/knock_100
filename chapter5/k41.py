#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import k40

class Chunk:
    def __init__(self, morph, dst, srcs):
        self.surface = 
        self.dst = 
        self.srcs = 


def main():
    path = 'neko.txt.cabocha'
    count = 0
    output = []
    with codecs.open(path, 'r') as fin:
        for line in fin:
            if line.strip() == 'EOS':
                count += 1
                if count == 3:
                    break
            elif count == 2:
                if line.split(' ')[0] != '*':
                    surface, w_info = line.split('\t')
                    ilist = w_info.split(',')
                    output.append(Morph(surface, ilist[6], ilist[0], ilist[1]))
    for w in output:
        print(w.surface, w.base, w.pos, w.pos1)

if __name__ == '__main__':
    main()
