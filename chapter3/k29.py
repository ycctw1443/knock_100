#!/usr/bin/env python
#-- coding:utf-8 -*-
import codecs
import json
from io import StringIO
import re
import requests

def get_info_text(text):
    info_text = ""
    for line in text.split('}}')[0].split('\n'):
        info_text = text.rstrip('\n') + line if re.search(r'^\*',line) else text + line
    return re.sub(r'http(.*?)\n','\n',re.sub(r'[\[\]\'\'\*\{\}]|<(.*?)>|\{(.*?)\}|ファイル:','',info_text))

def main():
    with codecs.open('jawiki-country.json','r','utf-8') as fin:
        list = [json.load(StringIO(line)) for line in fin]
    text = '\n'.join([doc['text'] for doc in list if doc['title'] == 'イギリス'])
    dict = {info[0]:info[1] for info in re.findall(r'\|(.*?)\s=\s(.*?)\n',get_info_text(text))} 
    params = {'action': 'query', 'prop': 'imageinfo', 'format': 'json', 'iiprop': 'url', 'titles': 'Image:{0}'.format(dict[u'国旗画像'].split('|')[0])}
    api = requests.get("https://en.wikipedia.org/w/api.php?action=query&titles=Main%20Page&prop=revisions&rvprop=content&format=json", params=params).json()
    print(api['query']['pages']['23473560']['imageinfo'][0]['url'])

if __name__ == '__main__':
    main()
