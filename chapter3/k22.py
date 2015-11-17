#!/usr/bin/env python
#-- coding:utf-8 -*-
import re
import k20

def main():
    print('\n'.join([line.split('|')[0] for line in re.findall('\[\[Category:(.*?)\]\]',k20.get_json('jawiki-country.json'))]))

if __name__ == '__main__':
    main()
