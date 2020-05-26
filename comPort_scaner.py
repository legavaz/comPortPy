
import serial,time
import comPort_Sql,comPort_utils

# Чтение настроек из файла ini
setting = comPort_utils.setting()
setting.print_setting()

# Установка настроек
ser             = serial.Serial()
ser.port        = setting.port
ser.baudrate    = int(setting.baudrate)
ser.timeout     = int(setting.timeout)

# подключаем устройство
try:
    ser.open()
except serial.SerialException as e:
    print("Error:",e)
    serial = None    
    comPort_utils.exit_program('Ошибка подключения порта')
    exit(1)

# подключаем базу данных
db      =   comPort_Sql.db(setting.db)

while True:
    print('.')  
    resp = ser.readline()      
    if len(resp) > 5:
        mStr    =   resp.decode("utf-8")        
        db.regPropusk(mStr,setting.stanok)
        print(time.strftime('%H:%M:%S'),mStr)

comPort_utils.exit_program()
