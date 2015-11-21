#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    for line in k20.get_json('jawiki-country.json').split('\n'):
        if re.search('Category', line):
            print(line)

if __name__ == '__main__':
    main()
