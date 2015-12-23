#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import Morph


def get_morph(path):
    output = []
    with codecs.open(path, 'r') as fin:
        c_list = ''.join(line for line in fin)
    mo_list = (sentence.strip() for sentence in c_list.split('EOS\n'))
    for sentence in mo_list:
        if not sentence:
            output.append([''])
            continue
        output.append([Morph.Morph(word)
                       for word in sentence.split('\n')
                       if word[0] != '*' and word[0] != '　'])
    return output


def main():
    morph = get_morph('neko.txt.cabocha')
    for w in morph[2]:
        print(w.surface, w.base, w.pos, w.pos1)

if __name__ == '__main__':
    main()
