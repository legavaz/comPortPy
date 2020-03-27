# https://github.com/legavaz/comPortPy.git
import serial
import sys,time
import sqlite3

ser             = serial.Serial()
ser.port        = "com7"
ser.baudrate    =  9600
ser.timeout     = 1
# ---------------------

# try to connect
try:
    ser.open()
except serial.SerialException as e:
    print("Error:",e)
    serial = None
    exit(1)


conn = sqlite3.connect("checkStaff.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

try:
    # Создание таблицы
    cursor.execute("""CREATE TABLE checkStaff
                  (propusk text, timeStr text, timeInt text)
               """)
except:
    print('sql : ok')


def removeFix(mString=""):
    mString =   mString.replace("x",'')
    mString =   mString.replace("\r\n",'')
    return mString

def regInDb(propusk):

    # Вставляем данные в таблицу
    command = """INSERT INTO checkStaff
                  VALUES ('%propusk%', '%timeStr%', '%timeInt%')"""
    command = command.replace('%propusk%', propusk)
    command = command.replace('%timeStr%', time.strftime('%H:%M:%S'))
    command = command.replace('%timeInt%', str(time.time()))
    cursor.execute(command)

    # Сохраняем изменения
    conn.commit()


while True:
    print('.')  
    resp = ser.readline()      
    if len(resp) > 5:
        mStr    =   resp.decode("utf-8")
        mStr    =   removeFix(mStr)
        regInDb(mStr)
        print(time.strftime('%H:%M:%S'),mStr)


print('exit - ok')

