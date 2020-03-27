
import sqlite3
import time

conn = sqlite3.connect("checkStaff.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()

try:
    # Создание таблицы
    cursor.execute("""CREATE TABLE checkStaff
                  (propusk text, timeStr text, timeInt text)
               """)
except:
    print('sql : ok')


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


propusk =   input(' введите строку: ')
regInDb(propusk)

print('ok')
