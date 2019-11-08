# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:59:39 2019

@author: Ricardo
"""

from tkinter import *
import serial, time
lectura = []

def botonLeer():
    global lectura
    arduino = serial.Serial('COM3',9600)
    time.sleep(2)
    datoNumeros = entradaDatos.get()
    largo = len(datoNumeros)
    try:        
        arduino.write(b'e')
        for i in range(int(datoNumeros)):
            lectura.append(arduino.readline()) 
        entradaDatos.delete(0,largo)                         
    except:
        messagebox.showerror('Error de datos', message = 'Los datos ingresados no son números enteros')
        entradaDatos.delete(0,largo)
    arduino.close()
    
def botonGuardar():
    if lectura != []:
        nombre = entradaArchivo.get()
        largo2 = len(nombre)
        if largo2 != None:
            nombredelArchivo = (entradaArchivo.get()+'.txt')
            archivo = open(nombredelArchivo,'w')
            archivo.write(str(lectura))
            archivo.close()
            entradaArchivo.delete(0,largo2)
    else:
        messagebox.showerror('Error de llenado', message = 'Los datos ingresados no están completos')
            

ventana = Tk()

frame1 = Frame(ventana)
frame1.pack()

leer = Button(frame1, text = 'Leer', command = botonLeer)
leer.pack(side = BOTTOM)

entradaDatos = Entry(frame1)
entradaDatos.pack(side = BOTTOM)

numeroDatos = Label(frame1, text = 'Número de datos:')
numeroDatos.pack(side = BOTTOM)


frame2 = Frame(ventana)
frame2.pack()

guardar = Button(frame2, text = 'Guardar', command = botonGuardar)
guardar.pack(side = BOTTOM)

entradaArchivo = Entry(frame2)
entradaArchivo.pack(side = BOTTOM)

nombreArchivo = Label(frame2, text = 'Nombre del archivo:')
nombreArchivo.pack(side = BOTTOM)


ventana.mainloop()
