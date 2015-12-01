#!/usr/bin/env python
# -- coding:utf-8 -*-
import codecs
import json
from io import StringIO


def get_json(path):
    with codecs.open(path, 'r', 'utf-8') as fin:
        i_list = [json.load(StringIO(line)) for line in fin]
    return '\n'.join(doc['text'] for doc in i_list if doc['title'] == 'イギリス')


def main():
    print(get_json('jawiki-country.json'))

if __name__ == '__main__':
    main()
