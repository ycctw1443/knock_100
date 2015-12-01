#!/usr/bin/env python
# -- coding:utf-8 -*-

str1 = "パトカー"
str2 = "タクシー"
print(''.join(s1 + s2 for (s1, s2) in zip(str1, str2)))
