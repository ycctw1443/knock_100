#!/usr/bin/env python
# -- coding:utf-8 -*-


def cipher(input_words):
    return ''.join(str(219 - ord(char)) if char.islower() else char
                   for char in input_words)


def main():
    input_words = input()
    print(cipher(input_words))

if __name__ == '__main__':
    main()
