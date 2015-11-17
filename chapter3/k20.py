#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import json
from io import StringIO

def main():
    with codecs.open('jawiki-country.json','r','utf-8') as fin: 
        list = [json.load(StringIO(line)) for line in fin]
        print('\n'.join([doc['text'] for doc in list if doc['title'] == 'イギリス']))

if __name__ == '__main__':
    main()
