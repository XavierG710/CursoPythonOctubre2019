# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 08:59:58 2019

@author: yocoy
"""

class Autos:
    
    color = ''
    tamaño = ''
    marca = ''
    modelo = ''
    numeroDePuertas = 5
    velocidad = 100
    
    def avanzar(self):
        self.velocidad += 10
        
    def arrancar(self):
        print(self.modelo + " está arrancando")
        
auto1 = Autos() #Crear o instanciar un objeto
auto1.modelo = 'Vento'
print(auto1.modelo)
auto1.arrancar()

auto2 = Autos()
auto2.modelo = 'Spark'
print(auto2.modelo)
print(auto1.modelo)

    