# -*- coding: utf-8 -*-
"""
Created on Sat Nov  2 09:26:41 2019

@author: yocoy
"""

import serial, time

arduino = serial.Serial('COM7', 9600)
time.sleep(4)
arduino.write(b'e')
arduino.close()
