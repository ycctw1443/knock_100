#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


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
