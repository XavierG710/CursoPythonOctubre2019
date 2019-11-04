# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:16:42 2019

@author: yocoy
"""

from tkinter import *
from tkinter import messagebox

def holaMundo():
    datos = entrada.get()
    entrada.delete(0, len(datos))
    messagebox.showinfo("Mensaje Enviado", message = datos)
    
root = Tk()

frame = Frame(root)
frame.pack()

boton = Button(frame, text = 'Botón', command = holaMundo)
boton.pack(side = BOTTOM)

entrada = Entry(frame)
entrada.pack(side = RIGHT)

etiqueta = Label(frame, text = 'Usuario:')
etiqueta.pack()


root.mainloop()