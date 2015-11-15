#!/usr/bin/env python
#-- coding:utf-8 -*-

#保存するが嫌なので分割して表示するだけにしました。
import codecs
import math
def main():
    with codecs.open('hightemp.txt','r','utf-8') as fin:
        list = [line for line in fin]
    try:
        n = len(list) / int(input())
        if(int(n) != n):
            raise Exception('行数が分割数で割りきれません')
        print(''.join([str + "分割\n" if (i+1) % n == 0 and (i+1) != len(list) else str for i,str in enumerate(list)]))
    except Exception as e:
        print(e)

if __name__ == '__main__':
    main()
