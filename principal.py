from tkinter import *
import serial, time, threading
lista=[]

def ChecarPuerto():
    global SerialPort
    global NumDatos
    ArduinoEstaConectado = False
    NumDatos.delete(0,len(NumDatos.get()))
    NumDatos.insert(0,"Buscando Arduino")
    while not ArduinoEstaConectado:
        for i in range(20):
            try:
                serial.Serial("COM"+str(i+1), 9600)
                Puerto = "COM"+str(i+1)
                ArduinoEstaConectado = True
                NumDatos.delete(0,len(NumDatos.get()))
                NumDatos.insert(0,"Arduino Encontrado")
                SerialPort = Puerto
            except:
                pass

def GuardarDatos():
    global lista
    global Archivo
    NombreDeArchivo = Archivo.get()
    try:
        if NombreDeArchivo[len(NombreDeArchivo)-4] == "." and NombreDeArchivo[len(NombreDeArchivo)-3] == "t" and NombreDeArchivo[len(NombreDeArchivo)-2] == "x" and NombreDeArchivo[len(NombreDeArchivo)-1] == "t":
            try:
                archivo = open(NombreDeArchivo,"a")
                archivo.write("\n")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
            except:
                archivo = open(NombreDeArchivo,"w")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
        else:
            try:
                archivo = open(NombreDeArchivo+".txt","a")
                archivo.write("\n")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
            except:
                archivo = open(NombreDeArchivo+".txt","w")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
    except:
        if len(NombreDeArchivo) > 0:
            try:
                archivo = open(NombreDeArchivo+".txt","a")
                archivo.write("\n")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
            except:
                archivo = open(NombreDeArchivo+".txt","w")
                for i in range(len(lista)):
                    try:
                        archivo.write(str(int(lista[i]))+" ")
                    except:
                        pass
                archivo.close()
        else:
            Archivo.delete(0,len(Archivo.get()))
            Archivo.insert(0,"Ingrese un nombre de archivo válido")

def CrearLista():
    global lista
    global SerialPort
    arduino = serial.Serial(SerialPort, 9600)
    time.sleep(4)
    lista = []
    try:
        for i in range(int(NumDatos.get())):
            lista.append(arduino.readline())
    except:
        print("Ingrese un valor valido")
    arduino.close()

def mostrarDatos():
    global lista
    if len(lista) > 0:
        print("Estos son los datos almacenados: ")
        for i in range(len(lista)):
            print(str(i+1)+") "+str(int(lista[i])))
        print("\n")
    else:
        print("No hay ningún dato exitente")

Ventana = Tk()
Ventana.title("Mi primer ventana")
buscarArduino = threading.Thread(target = ChecarPuerto)
frame = Frame(Ventana)
frame.pack(ipadx = 50, ipady = 50, side = BOTTOM)
etiqueta = Label(frame,text = "Número de datos:")
etiqueta.pack()
NumDatos = Entry(frame)
NumDatos.pack(ipadx = 10, ipady = 5)
buscarArduino.start()
LeerDatos = Button(frame, text = "Leer datos", command = CrearLista)
LeerDatos.pack(ipadx = 10, ipady = 5)
espacio2 = Label(frame,text = "")
espacio2.pack()
etiquetaNombreDeA = Label(frame,text = "Nombre de archivo:")
etiquetaNombreDeA.pack()
Archivo = Entry(frame)
Archivo.pack(ipadx = 10, ipady = 5)
Guardar = Button(frame, text = "Guardar", command = GuardarDatos)
Guardar.pack(ipadx = 10, ipady = 5)
espacio3 = Label(frame,text = "")
espacio3.pack()
Mostrar = Button(frame, text = "Mostrar", command = mostrarDatos)
Mostrar.pack(ipadx = 30, ipady = 5)
Ventana.geometry("500x400")
Ventana.mainloop()
