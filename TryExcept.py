# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 10:57:50 2019

@author: yocoy
"""

#try:
#    x = float(input('-> '))
#    x = 4/0
#except ZeroDivisionError:
#    print("Dividiste entre 0 :(")
#except ValueError:
#    print("Pusiste una letra :(")

while True:
    try:
        x = float(input('-> '))
        break
    except:
        print("Valor inválido, intenta otra vez...")