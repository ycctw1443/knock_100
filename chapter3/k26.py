#!/usr/bin/env python
#-- coding:utf-8 -*-
import re
import k20

def get_info(text):
    info_text =''
    for line in text.split('}}')[0].split('\n'):
        info_text = text.rstrip('\n') + line if re.search(r'^\*',line) else text + line
    return re.sub(r'\'','',info_text)

def main():
    dict = {info[0]:info[1] for info in re.findall(r'\|(.*?)\s=\s(.*?)\n',get_info(k20.get_json('jawiki-country.json')))} 
    print(dict)

if __name__ == '__main__':
    main()
