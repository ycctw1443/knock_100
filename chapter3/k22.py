#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    for line in re.findall('\[\[Category:(.*?)\]\]', k20.get_json(path)):
        print(line.split('|')[0])

if __name__ == '__main__':
    main()
