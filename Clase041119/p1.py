# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 10:53:43 2019

@author: yocoy
"""

x = b'\r9\n'
y = str(x).replace('b', '').replace("'", '').replace('r', '').replace('n', '').replace("\\", '')

z = int(y)

print(type(z))
print(y)
print(x)
print(z)