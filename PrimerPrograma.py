# -*- coding: utf-8 -*-
"""
Curso Python ARACT Mayo 2019
Programa: Explicación de los conceptos básicos de Python
@author: Yocoyani Ehecatzin Pérez Ayala 
Todos los derechos reservados
"""
#Importar bibliotecas de Python
import math
from math import ceil
from math import floor

#Esto es un comentario

print('Hola mundo')


#Uso de variables y operaciones básicas

x = 0
print (x)
x = '\nEste es el mejor curso de Python'
z = ' y yo lo certifico'

print(x)
print(x+z)
y = x*5
print(y, end = '\n\n')

n1 = 56.7
n2 = 78
n3 = 67

print(n1*n2)
print(n2*n3)
#print(2/0)
print(n2/n3)
print(n2//n3, end = '\n\n')

print(2**6)
print(pow(2,6))
print(math.sqrt(2), end = '\n\n')

round(1.4256)
round(1.7666)
ceil(1.4256)
floor(1.7666)



s = 4 + 7j
t = 6 + 5j
print(s)
print(s*t)

#Estructuras funcionales
if 'Juan' == 'JUAN':
    print('Son iguales')
else:
    print('Son diferentes')
    
if 2 == 3:
    print('Son diferentes')
elif 2 < 3:
    print('2 es mayor que 3')
elif 3 > 2:
    print('3 es mayor que 2')


for i in range(10):
    print(i)
    
nombre = 'Soy el mejor programador en Python'

for n in nombre:
    print(n, end = '')
    
for n in range(len(nombre)):
    print(n)

print('\n')

i = 0
while i < 3:
    print(i)
    i+=1

try: 
    print(9/0)
except :
    print('Error Matemático')
    
#Lectura desde teclado

lectura = input('Escribe aqui: ')
print(lectura)

n1 = int(input('n1: '))
n2 = int(input('n2: '))

print(n1/n2)
