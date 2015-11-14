#!/usr/bin/env python
#-- coding:utf-8 -*-

def bigram(input):
    return([input[i:i+2] for i in range(len(input)-1)])

def main():
    str = "I am an NLPer"
    print(bigram(str),bigram(str.split(" ")))

if __name__ == '__main__':
    main()
