# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 09:06:46 2019

@author: yocoy
"""

import serial, time 

arduino = serial.Serial('COM7',9600)
time.sleep(4)

lectura = []

arduino.write(b'e')

for i in range(100):
    lectura.append(arduino.readline())

print(lectura)

arduino.close()