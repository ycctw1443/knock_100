#!/usr/bin/env python
# -- coding:utf-8 -*-
# 保存するが嫌なので分割して表示するだけにしました。
import codecs


def main():
    with codecs.open('hightemp.txt', 'r', 'utf-8') as fin:
        input_list = [line for line in fin]
    try:
        n = len(input_list) / int(input())
        if(int(n) != n):
            raise Exception('行数が分割数で割りきれません')
        for i, s in enumerate(input_list):
            k = i + 1
            print(s+'分割\n' if k % n == 0 and k != len(input_list) else s)
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
