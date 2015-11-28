#!/usr/bin/env python
# -- coding:utf-8 -*-


def bigram(input_str):
    return([input_str[i:i+2] for i in range(len(input_str)-1)])


def main():
    x = bigram('paraparaparadise')
    y = bigram('paragraph')
    print(list(set(x+y)))
    print(list(set([term for term in x if term in y])))
    print(list(set([term for term in x if term not in y])))
    print(True if 'se' in x or 'se' in y else False)

if __name__ == '__main__':
    main()
