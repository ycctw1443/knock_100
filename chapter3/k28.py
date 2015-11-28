#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20
import k25


def main():
    path = 'jawiki-country.json'
    p = re.compile(r'[\[\]\'\'\*\{\}]|<(.*?)>|\{(.*?)\}|ファイル:|\(\&(.*?)\)')
    text = re.sub(r'http(.*?)\n', '\n', re.sub(p, '', k20.get_json(path)))
    print(k25.get_info_dict(text))

if __name__ == '__main__':
    main()
