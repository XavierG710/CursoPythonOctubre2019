# -*- coding: utf-8 -*-
"""
Created on Sun Oct 20 10:56:53 2019

@author: yocoy
"""

nombreArchivo = "NuevoArchivo.txt"

#archivo = open(nombreArchivo, 'r')
##
##texto = archivo.read()
#
#texto1 = []
#
#texto1.append(archivo.readline().split(' '))
#texto1.append(archivo.readline().split(' '))
#texto1.append(archivo.readline().split(' '))
##
##texto1 = archivo.readlines()
#
#print(texto1)
#
#archivo.close()
#
#print(len(texto1[0][0]))
texto = 'Borro el mensaje anterior'
archivo = open(nombreArchivo, 'w')
#archivo2 = open('A2.txt', 'w')
archivo.write(texto)

archivo.close()
#archivo2.close()