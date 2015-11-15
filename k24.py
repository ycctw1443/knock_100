#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import json
from io import StringIO
import re

def main():
    with codecs.open('jawiki-country.json','r','utf-8') as fin:
        list = [json.load(StringIO(line)) for line in fin]
        text = '\n'.join([doc['text'] for doc in list if doc['title'] == 'イギリス'])
        print('\n'.join([line[1] for line in re.findall('\[\[(File|ファイル):(.*?)\|',text)]))

if __name__ == '__main__':
    main()
