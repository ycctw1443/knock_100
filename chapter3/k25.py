#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    dict = {}
    for info in re.findall(r'\|(.*?)\s=\s(.*?)\n', k20.get_json(path)):
        dict[info[0]] = info[1]
    print(dict)

if __name__ == '__main__':
    main()
