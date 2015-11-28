#!/usr/bin/env python
# -- coding:utf-8 -*-


def bigram(sentence):
    return([sentence[i:i+2] for i in range(len(sentence)-1)])


def main():
    sentence = 'I am an NLPer'
    print(bigram(sentence), bigram(sentence.split(' ')))

if __name__ == '__main__':
    main()
