#!/usr/bin/env python
# -- coding:utf-8 -*-
import re

sentence = '''
Now I need a drink, alcoholic of course, afterthe heavy lectures \
involving quantum mechanics.
'''.strip()
print([len(re.sub(r', .', '', x)) for x in sentence.split(' ')])
