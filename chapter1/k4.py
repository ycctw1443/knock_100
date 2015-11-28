#!/usr/bin/env python
# -- coding:utf-8 -*-

sentence = '''
Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations \
Might Also Sign Peace Security Clause. Arthur King Can.
'''.strip()
dic = {}
for i, v in enumerate(sentence.split()):
    dic[v[:1 if i+1 in [1, 5, 6, 7, 8, 9, 15, 16, 19] else 2]] = i+1
print(sorted(dic.items(), key=lambda x: x[1]))
