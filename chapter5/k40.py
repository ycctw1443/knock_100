#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs


class Morph:
    def __init__(self, surface, base, pos, pos1):
        self.surface = surface
        self.base = base
        self.pos = pos
        self.pos1 = pos1


def get_morph(path):
    output = []
    with codecs.open(path, 'r') as fin:
        c_list = ''.join([line for line in fin])
    mo_list = [sentence.strip() for sentence in c_list.split('EOS\n')]
    for sentence in mo_list:
        if not sentence:
            output.append([''])
            continue
        output.append([Morph(word.split()[0],
                             word.split()[1].split(',')[6],
                             word.split()[1].split(',')[0],
                             word.split()[1].split(',')[1])
                       for word in sentence.split('\n')
                       if word[0] != '*' and word[0] != '　'])
    return output


def main():
    output = get_morph('neko.txt.cabocha')
    for w in output[2]:
        print(w.surface, w.base, w.pos, w.pos1)

if __name__ == '__main__':
    main()
