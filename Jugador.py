# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:15:13 2019

@author: yocoy
"""

class Jugador():
    
    def __init__(self, nombre, deporte, equipo):
        self.nombre = nombre
        self.deporte = deporte
        self.equipo = equipo
        
    def jugando(self):
        print(self.nombre + " esta jugando " + self.deporte + " en el equipo "  + self.equipo)
        
        
jugador1 = Jugador('Michael Jordan', 'Basquetbol', 'Bulls')      
jugador1.jugando()  
        
