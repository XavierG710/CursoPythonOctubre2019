# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 08:04:11 2019

@author: yocoy
"""

import serial, time

arduino = serial.Serial('COM7', 9600)
time.sleep(4)

lectura = []

for i in range(100):
    lectura.append(arduino.readline())
arduino.close()

print(lectura)