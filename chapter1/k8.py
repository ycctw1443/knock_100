#!/usr/bin/env python
#-- coding:utf-8 -*-

def cipher(words):
    return ''.join([str(219 - ord(char)) if char.islower() else char for char in words])

def main():
    input_word = input()
    print(cipher(input_word))

if __name__ == '__main__':
    main()
