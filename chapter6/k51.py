#!/usr/bin/env python
# -- coding:utf-8 -*-
import k50


def get_words(path):
    output = []
    text = k50.get_text(path)
    output = [word for sentence in text for word in sentence.split(' ')]
    output.append('')
    return output


def main():
    text = get_words('nlp.txt')
    for word in text:
        print(word)

if __name__ == '__main__':
    main()
