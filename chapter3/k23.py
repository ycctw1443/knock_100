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
        print('\n'.join([re.sub(r'\s','',line[1])+' '+str(len(line[0])-1) for line in re.findall('(={2,})(.*?)={2,}',text)]))

if __name__ == '__main__':
    main()
