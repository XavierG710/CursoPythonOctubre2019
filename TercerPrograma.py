# -*- coding: utf-8 -*-
"""
Curso Python ARACT Mayo 2019
Programa: Explicación de funciones y objetos
@author: Yocoyani Ehecatzin Pérez Ayala 
Todos los derechos reservados
"""

#Objetos y funciones

def lecturaNumeros(cantidad): #Declaracion de funciones
    numeros = []
    for i in range(cantidad):
        while 1:
            try:
                numeros.append(int(input('n'+str(i+1)+': ')))
                break
            except: 
               print('Caracter inváilido, intenta otra vez')
    
    return numeros #Valor de retorno de funciones, pueden retornar incluso listas o tuplas

class Calculadora(): #Declaracion de clases
    
    def sumar(self): #Declaración de métodos, pueden recibir parámetros al igual que las funciones
        n1,n2 = lecturaNumeros(2)
        return n1+n2 #Al igual que las funciones, los métodos pueden regresar valores
    
    def restar(self):
        n1,n2 = lecturaNumeros(2)
        return n1-n2
    
    def dividir(self):
        n1,n2 = lecturaNumeros(2)
        if n2 != 0:
            return n1/n2
        else:
            return 'Error, división entre 0'
        
    def multiplicar(self):
        n1,n2 = lecturaNumeros(2)
        return n2*n1;
    
class Menu():
    
    def __init__(self, opciones, acciones, objetos = None): #Declaración de un constructor que índica los atributos que tendrá un objeto
        self.opciones = opciones #Self hace referencia a atributos del mismo objeto
        self.acciones = acciones
        self.objetos = objetos #Como está igualado a None, índica que puede no recibirse ese valor
        
    def correrMenu(self):
        while 1:
            Texto = 'Selecciona una opción:\n'
            for i in range(len(self.opciones)):
                Texto = Texto + str(i+1) + ')' + self.opciones[i]+'\n' 
            Texto = Texto + '\na)Salir\n--> '
            opcion = input(Texto)
            
            for i in range(len(self.opciones)):
                if opcion == str(i+1):
                    print (eval('self.objetos'+self.acciones[i]))
            
            if opcion == 'a':
                break

def main():
    calc = Calculadora() #Creación de un objeto de la clase correspondiente
    
    opciones = ['Sumar','Restar','Multiplicar','Dividir']
    acciones = ['.sumar()','.restar()','.multilpicar()','.dividir()']
    
    men = Menu(opciones,acciones, objetos = calc) #Ejemplo de creación de objetos con constructor
    men.correrMenu() #Llamada de métodos

main()