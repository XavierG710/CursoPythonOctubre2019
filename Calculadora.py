# -*- coding: utf-8 -*-
"""
Created on Sun Oct 13 09:52:09 2019

@author: yocoy
"""

class Calculadoras():
    
    def __init__(self, numero1, numero2, numeroCaluladora):
        self.numero1 = numero1
        self.numero2 = numero2
        self.numeroCalculadora = numeroCaluladora
        
    def sumar(self):
        print("Calculadora " + str(self.numeroCalculadora) +" está sumando")
        print("Resultado: " + str(self.numero1+self.numero2))
    
    def restar(self):
        print("Calculadora " + str(self.numeroCalculadora) +" está restando")
        print("Resultado: " + str(self.numero1-self.numero2)) 
    
    def multiplicar(self):
        print("Calculadora " + str(self.numeroCalculadora) +" está multiplicando")
        print("Resultado: " + str(self.numero1*self.numero2))
    
    
    def dividir(self):
        print("Calculadora " + str(self.numeroCalculadora) +" está sumando")
        print("Resultado: " + str(self.numero1/+self.numero2))

while True:
    print("\tMenú")
    print("1)Sumar")
    print("2)Restar")
    print("3)Multiplicar")
    print("4)Dividir")
    print("5)Salir")
    
    seleccion = []
    seleccion.append(int(input('Primera elección: ')))
    seleccion.append(int(input('Segunda elección: ')))
    
    if seleccion[0] == 5 or seleccion[1] == 5:
        break
    
    calculadora = []
    
    for i in range(len(seleccion)):
        print("Operación "+str(i+1))
        n1 = float(input('n1-> '))
        n2 = float(input('n2-> '))
        calculadora.append(Calculadoras(n1,n2,i+1))
        
    for i in range(len(seleccion)):
        if seleccion[i] == 1:
            calculadora[i].sumar()
        elif seleccion[i] == 2:
            calculadora[i].restar()
        elif seleccion[i] == 3:
            calculadora[i].multiplicar()
        elif seleccion[i] == 4:
            calculadora[i].dividir()