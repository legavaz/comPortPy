#!/usr/bin/env python3
# coding:utf8

import serial
import time
import sys


# connect to serial port
ser = serial.serial_for_url("com6", do_not_open=True)
# ser = serial.Serial("com6")

try:
  ser.open()
except serial.SerialException as e:
  sys.stderr.write(
  'Could not open serial port {}: {}\n'.format(ser.name, e))
  sys.exit(1)

print('ver serial:',serial.__version__)
# serial.Serial.open()
PORT    = '"/dev/ttyUSB6"'
timeout = 1

if __name__ == '__main__':
  try:
    port    = serial.Serial(
    port    = 'COM6',\
    baudrate=9600,\
    parity  =serial.PARITY_NONE,\
    stopbits=serial.STOPBITS_ONE,\
    bytesize=serial.EIGHTBITS,\
    timeout =0)
  except serial.SerialException:
    print('Соединение не удалось')
    exit(1)

  port.flushOutput()
  port.flushInput()

  # Послать запрос
  cmd = bytes('ati\r', 'utf-8')
  port.write(cmd)

  time.sleep(0.1)

  # Принять ответ и вывести его на консоль
  while True:
    print('.')
  
    resp = port.readline()
  
    # Вариант вывода 1
    if len(resp) > 0:
      print('[{0:d}] = '.format(len(resp)), end = '')
      for b in resp:
        print('0x{0:02X} '.format(b), end='')
  
    '''
    # Вариант вывода 2
    string = str(port.readline())
    if len(string) > 0:
      print('[{0:d}] = '.format(len(string)), end = '')
      for ch in string:
        print('0x{0:02X} '.format(ord(ch)), end='')
    '''
  
    '''
    # Вариант вывода 3
    string = str(port.readline())
    if len(string) > 0:
      print('[{0:d}] = '.format(len(string)), end = '')
      print(string)
   '''
