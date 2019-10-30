# -*- coding: utf-8 -*-
"""
Created on Sun Oct 27 11:23:41 2019

@author: yocoy
"""

import EditorPersonajes as ep

def main():
    ep.crearArchivo()
    while True:
        print('\t Menú')
        print('1)Crear personaje')
        print('2)Editar personaje')
        print('3)Borrar personaje')
        print('Otro->Salir')
        
        seleccion = input('Selección: ')
        
        if seleccion == '1':
            ep.crearPersonaje()
        elif seleccion == '2':
            ep.editarPersonajes()
        elif seleccion == '3':
            ep.borrarPersonaje()
        else:
            break
main()
    
    