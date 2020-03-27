

import serial
import sys

ser             = serial.Serial()
ser.port        = "com7"
ser.baudrate    =  9600
ser.timeout     = 1

# try to connect
try:
    ser.open()
except serial.SerialException as e:
    print("Error:",e)
    serial = None
    exit(1)


while True:
    print('.')
  
    resp = ser.readline()
  
    # Вариант вывода 1
    if len(resp) > 0:
        print(resp)


print('exit - ok')

