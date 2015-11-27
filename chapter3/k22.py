#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    print('\n'.join([
        item.split('|')[0]
        for item in re.findall('\[\[Category:(.*?)\]\]', k20.get_json(path))]))

if __name__ == '__main__':
    main()
