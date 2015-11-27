#!/usr/bin/env python
# -- coding:utf-8 -*-
import re
import k20


def main():
    path = 'jawiki-country.json'
    pattern = re.compile('\[\[(File|ファイル):(.*?)\|')
    print('\n'.join([line[1]
                     for line in re.findall(pattern, k20.get_json(path))]))

if __name__ == '__main__':
    main()
