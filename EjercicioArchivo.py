# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 11:44:34 2019

@author: yocoy
"""

archivo = open('ArchivoDatos.txt', 'r')
#
#cadena = '125,18,15,6\n75,89,150\n54,78,90'
#archivo.write(cadena)
#
#archivo.close()

texto = archivo.readlines()
archivo.close()

textoEditable = texto[0].split(',')
indice = textoEditable.index('18')
textoEditable.remove('18')
textoEditable.insert(indice, '20')

print(textoEditable)