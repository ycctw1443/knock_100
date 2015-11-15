#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import json
from io import StringIO
import re

def get_info_text(text):
    info_text =''
    for line in text.split('}}')[0].split('\n'):
        info_text = text.rstrip('\n') + line if re.search(r'^\*',line) else text + line
    return info_text

def main():
    with codecs.open('jawiki-country.json','r','utf-8') as fin:
        list = [json.load(StringIO(line)) for line in fin]
        text = '\n'.join([doc['text'] for doc in list if doc['title'] == 'イギリス'])
        dict = {info[0]:info[1] for info in re.findall(r'\|(.*?)\s=\s(.*?)\n',get_info_text(text))} 
        print(dict)

if __name__ == '__main__':
    main()
