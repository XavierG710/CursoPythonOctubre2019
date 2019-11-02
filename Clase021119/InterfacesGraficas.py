# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:44:52 2019

@author: yocoy
"""

from tkinter import *

def holaMundo():
    print(entrada.get())
    #entrada.insert(0,'Gracias')
    messagebox.showerror(message = entrada.get())
    entrada.delete(0, len(entrada.get()))
    
root = Tk()

frame = Frame(root)
frame.pack(side = BOTTOM)

boton1 = Button(frame, text = 'Boton', command = holaMundo)
boton1.pack(side = BOTTOM)

etiqueta = Label(frame, text = 'Soy una etiqueta')
etiqueta.pack()

entrada = Entry(frame)
entrada.pack(side = RIGHT)

root.mainloop()
