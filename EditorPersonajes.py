# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 09:46:40 2019

@author: yocoy
"""
nombreArchivo = 'Personajes.txt'

def crearArchivo():
    archivo = open(nombreArchivo, 'a')
    archivo.close()

def crearPersonaje():
    
    nombre = input('Nombre: ').lower()   
    
    archivo = open(nombreArchivo, 'r')
    lectura = archivo.readlines()
    archivo.close()
    for i in range(len(lectura)):
        lectura[i] = lectura[i].split(',')
        
    for i in range(len(lectura)):
        if lectura[i][0] == nombre:
            print('Personajes repetido, no se creará')
            return     
    ataque = input('Ataque: ')
    defensa = input('Defensa: ')
    
    datoAgregado = nombre + ',' + ataque + ','+defensa + '\n'
    
    archivo = open(nombreArchivo, 'a')
    archivo.write(datoAgregado)
    archivo.close()
 
def editarPersonajes():
    archivo = open(nombreArchivo, 'r')
    lectura = archivo.readlines()
    archivo.close()
    
    for i in range(len(lectura)):
        lectura[i] = lectura[i].split(',')
        
    nombre = input('Nombre a buscar: ').lower()
    
    indice = -1
    for i in range(len(lectura)):
        if lectura[i][0] == nombre:
            indice = i
    if indice == -1:
        print('No existe personaje')
        return
    ataque = input('Ataque nuevo: ')
    defensa = input('Defensa nueva: ')
    
    lectura[indice][1] = ataque
    lectura[indice][2] = defensa+'\n'
    
    datosActualizado = ''
    
    for i in range(len(lectura)):
        for j in range(len(lectura[i])):
            if j == len(lectura[i])-1:
                datosActualizado += lectura[i][j]
            else:
                datosActualizado += lectura[i][j]+','
    archivo = open(nombreArchivo, 'w')
    archivo.write(datosActualizado)
    archivo.close()

def  borrarPersonaje():
    archivo = open(nombreArchivo, 'r')
    lectura = archivo.readlines()
    archivo.close()
    
    for i in range(len(lectura)):
        lectura[i] = lectura[i].split(',')
    
    nombre = input('Personaje a eliminar: ').lower()
    
    indice = -1
    for i in range(len(lectura)):
        if lectura[i][0] == nombre:
            indice = i
    if indice == -1:
        print('No existe personaje')
        return
    
    lectura.remove(lectura[indice])
    
    datosActualizado = ''
    
    for i in range(len(lectura)):
        for j in range(len(lectura[i])):
            if j == len(lectura[i])-1:
                datosActualizado += lectura[i][j]
            else:
                datosActualizado += lectura[i][j]+','
    archivo = open(nombreArchivo, 'w')
    archivo.write(datosActualizado)
    archivo.close()
    
