#!/usr/bin/env python
#-- coding:utf-8 -*-

import re
str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
print([len(re.sub(r',.','',x)) for x in str.split(' ')])
