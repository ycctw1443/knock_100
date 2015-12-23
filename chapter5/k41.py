#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import Morph
import Chunk


def get_chunk(sentence):
    output = []
    dst = 0
    srcs = 0
    for word in sentence.split('\n'):
        if word[0] == '　':
            continue
        if word.split()[1].split(',')[0] == '記号':
            continue
        if word[0] == '*':
            dst = word.split()[2].rstrip('D')
            srcs = word.split()[1]
        else:
            output.append(Chunk.Chunk(Morph.Morph(word), dst, srcs))
    return output


def get_chunk_list(path):
    output = []
    with codecs.open(path, 'r') as fin:
        c_list = ''.join(line for line in fin)
    ch_list = [sentence.strip() for sentence in c_list.split('EOS\n')]
    for sentence in ch_list:
        if not sentence:
            output.append([''])
            continue
        output.append(get_chunk(sentence))
    return output


def main():
    result = get_chunk_list('neko.txt.cabocha')
    # ここからは出力のみ。確実にもっと簡略化できる。
    output = ''
    s_num = str(0)
    d_num = str(0)
    for c in result[7]:
        if c.srcs != s_num:
            print(output, d_num)
            s_num = c.srcs
            output = ''
        output += c.morphs.surface
        d_num = c.dst
        if c == result[7][-1]:
            print(output, d_num)

if __name__ == '__main__':
        main()
