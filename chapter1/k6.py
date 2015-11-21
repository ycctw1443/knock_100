#!/usr/bin/env python
# -- coding:utf-8 -*-


def bigram(input):
    return([input[i:i+2] for i in range(len(input)-1)])


def main():
    x = bigram('paraparaparadise')
    y = bigram('paragraph')
    print((list(set(x+y))))
    print((list(set([str for str in x if str in y]))))
    print((list(set([str for str in x if str not in y]))))
    print(True if 'se' in x or 'se' in y else False)

if __name__ == '__main__':
    main()
