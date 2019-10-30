# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 11:28:21 2019

@author: yocoy
"""
from random import randint

class Luchador:
    
    def __init__(self, nombre, ataque, defensa, vida):
        self.nombre = nombre
        self.ataque = ataque
        self.defensa = defensa
        self.vida = vida
        
    def atacar(self):
       print(self.nombre + " está atacando")
       return self.ataque
        
    def defender(self, ataqueOponente):
        print(self.nombre + " recibe ataque")
        daño = (ataqueOponente/self.defensa) * 100
        self.vida -= daño
    
    def morir(self):
        if self.vida <= 0: 
            print(self.nombre + " ha muerto")
            return True
        else: 
            return False
        
def controlJuego(personajes):
    turno = 0
    input('Presiona enter para empezar')
    while not personajes[0].morir() and not personajes[1].morir():
        probabilidad = randint(0,100)
        
        if turno % 2 == 0:
            print("Turno del primer jugador")
            if probabilidad > 35:
                ataqueHecho = personajes[0].atacar()
                personajes[1].defender(ataqueHecho)
        else:
            print("Turno del segundo jugador")
            if probabilidad > 35:
                ataqueHecho = personajes[1].atacar()
                personajes[0].defender(ataqueHecho)
        
        print('La vida de '+personajes[0].nombre+ ' es: '+str(personajes[0].vida))
        print('La vida de '+personajes[1].nombre + ' es: '+ str(personajes[1].vida))
        input('Presiona enter para seguir')
        turno += 1
        
def main():
    
    personajes = [Luchador('El jajas', 100, 100, 1000),Luchador('La sociedad', 500, 500, 1000), Luchador('Otro gato', 1000,1000,500),Luchador('Alfredo Adame',100,100,10000)]
    
    print("\t Menú")
    for i in range(len(personajes)):
        print(str(i+1)+')'+personajes[i].nombre)
    
    seleccion = []
    for i in range(2):
        while True:
            try:
                selTemp = int(input('Seleccion jugador'+str(i+1)+': '))
                if selTemp > len(personajes) or selTemp <= 0:
                    personajes[selTemp-1]
                seleccion.append(selTemp-1)
                break
            except:
                print("Selección inválida...")
    personajesElegidos = [personajes[seleccion[0]],personajes[seleccion[1]]]
    controlJuego(personajesElegidos)
    
main()
        