# -*- coding: utf-8 -*-
"""
Curso Python ARACT Mayo 2019
Programa: Explicación de listas
@author: Yocoyani Ehecatzin Pérez Ayala 
Todos los derechos reservados
"""

#Listas
listaNumeros = [1,2,3,4,5,6,7,8]
listaCaracteres = ['H','o','l','a']

print(listaNumeros)
print(listaCaracteres)

nuevaLista = listaNumeros+listaCaracteres

print(nuevaLista)
print(nuevaLista[6])

busqueda = nuevaLista.index('o')
print(busqueda)
nuevaLista.remove('H')
print(nuevaLista)
nuevaLista.append('a')
print(nuevaLista)
nuevaLista.clear()
print(nuevaLista)

nuevaLista = [x for x in range(10)]
print(nuevaLista)
nuevaLista.append(nuevaLista)
print(nuevaLista)
print(nuevaLista.pop())
print(nuevaLista)

