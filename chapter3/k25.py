#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def get_info_dict(text):
    pattern = r'\|(.*?)\s=\s(.*?)\n'
    return {info[0]: info[1] for info in re.findall(pattern, text)}


def main():
    path = 'jawiki-country.json'
    print(get_info_dict(k20.get_json(path)))

if __name__ == '__main__':
    main()
