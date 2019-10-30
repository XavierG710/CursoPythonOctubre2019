# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 08:14:39 2019

@author: yocoy
"""

nombreDeArchivo = 'ArchivoNumeros.txt'

archivo = open(nombreDeArchivo, 'r')

lectura = archivo.readlines()

archivo.close()

print(lectura)

for i in range(len(lectura)):
    lectura[i] = lectura[i].split(' ')
print(lectura)
    
for i in range(len(lectura)):
    lectura[i][1] = '20'

datosActualizados = ''

for i in range(len(lectura)):
    for j in range(len(lectura[i])):
        if j == len(lectura[i])-1:    
            datosActualizados += lectura[i][j]
        else:
            datosActualizados += lectura[i][j]+' '

archivo = open(nombreDeArchivo, 'w')
archivo.write(datosActualizados)
archivo.close()