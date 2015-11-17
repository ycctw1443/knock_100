#!/usr/bin/env python
#-- coding:utf-8 -*-
import re
import k20

def main():
    print('\n'.join([line[1] for line in re.findall('\[\[(File|ファイル):(.*?)\|',k20.get_json('jawiki-country.json'))]))

if __name__ == '__main__':
    main()
