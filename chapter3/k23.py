#!/usr/bin/env python
#-- coding:utf-8 -*-
import re
import k20

def main():
    print('\n'.join([re.sub(r'\s','',line[1])+str(len(line[0])-1) for line in re.findall('(={2,})(.*?)={2,}',k20.get_json('jawiki-country.json'))]))

if __name__ == '__main__':
    main()
