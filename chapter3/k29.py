#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import requests
import k20


def main():
    path = 'jawiki-country.json'
    dict = {}
    p = re.compile(r'[\[\]\'\'\*\{\}]|<(.*?)>|\{(.*?)\}|ファイル:|\(\&(.*?)\)')
    text = re.sub(r'http(.*?)\n', '\n', re.sub(p, '', k20.get_json(path)))
    for info in re.findall(r'\|(.*?)\s=\s(.*?)\n', text):
        dict[info[0]] = info[1]
    params = {'action': 'query',
              'prop': 'imageinfo',
              'format': 'json',
              'iiprop': 'url',
              'titles': 'Image:{0}'.format(dict[u'国旗画像'].split('|')[0])}
    uri = 'https://en.wikipedia.org/w/api.php?action=query&'
    uri += 'titles=Main%20Page&prop=revisions&rvprop=content&format=json'
    api = requests.get(uri, params=params).json()
    print(api['query']['pages']['23473560']['imageinfo'][0]['url'])

if __name__ == '__main__':
    main()
