#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    for line in re.findall('\[\[(File|ファイル):(.*?)\|', k20.get_json(path)):
        print(line[1])

if __name__ == '__main__':
    main()
