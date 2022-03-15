# -*- coding: utf-8 -*-
"""
Created on Sun Feb  6 14:52:16 2022

@author: loveboi
"""

import gym
import serial

import os
import gc
import time

ser = serial.Serial('COM5', baudrate=9600, timeout=1)
ser.reset_input_buffer()


arr = []
since = time.time()
while True:
    try:
        try:
            a0_value = int(ser.readline().decode().strip())
            print(a0_value)
            arr.append(a0_value)
            if ( time.time() - since ) > 60:
                print(len(arr)/60)
                ser.close()
                break
        except KeyboardInterrupt:
            print("KeyboardInterrupt")
            ser.close()
            break
        except:
            continue
    except Exception as e:
        print(e)
        ser.close()
        break
    except KeyboardInterrupt:
        print("KeyboardInterrupt")
        ser.close()
        break

ser.close()