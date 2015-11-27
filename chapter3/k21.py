#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    print('\n'.join([line for line in k20.get_json(path).split('\n')
                     if re.search('Category', line)]))

if __name__ == '__main__':
    main()
