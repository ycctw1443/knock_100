#!/usr/bin/env python
# -- coding:utf-8 -*-


def cipher(words):
    return ''.join([str(219 - ord(c)) if c.islower() else c for c in words])


def main():
    input_word = input()
    print(cipher(input_word))

if __name__ == '__main__':
    main()
