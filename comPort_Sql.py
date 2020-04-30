
# http://unetway.com/tutorial/sqlite/
# https://codernotes.ru/articles/bazy-dannyh-t-sql/sql-funkcii-kotorye-ponimaet-sqlite.html

# Запрос с именованными заполнителями
# sql     = "SELECT * FROM 'staffWork' WHERE export_bl=:export_bl;"
# db.cursor.execute(sql,{'export_bl':0})
# result  =   db.cursor.fetchall()

# Примеры запросов
# 1 запрос: Выборка для выгрузки в 1С со статусом: ({'export_bl':0})
# sql     = "SELECT * FROM 'staffWork' WHERE export_bl=:export_bl;"
# result  =   db.sqlQuery_fetch(sql,{'export_bl':1})

# **************************
# РАБОТА С ДАТАМИ В ЗАПРОСЕ
# select
#     julianday('now'),
#     julianday(time_str),
#     julianday('now') - julianday(time_str) as days
# from staffWork;

# *************************
# select
#     julianday('now'),
#     julianday(time_str),
#     24* (julianday(time_str) - julianday('now'))  as hour

# from staffWork;

# select
# test_id_int as id,
# DateTime,
# propusk_id_txt as propusk_id,
# CAST((julianday('now') - julianday(DateTime) ) as integer) as days_old
# from staffWork
# WHERE
# CAST((julianday('now') - julianday(DateTime) ) as integer) >15
# and export_bl<>0;

# *******1 запрос: Выборка для выгрузки в 1С со статусом: ({'export_bl':0})
# sql     = "SELECT * FROM 'staffWork' WHERE export_bl=:export_bl;"
# result  =   db.sqlQuery_fetch(sql,{'export_bl':1})

# *******2 запрос: Выборка для удаления старых записей: ({'export_bl':0})
# sql     = "SELECT * FROM 'staffWork' WHERE time_int<:start;"
# result  =   db.sqlQuery_fetch(sql,{'start':datetime.datetime.today()})

#  3  # Удаление записей
# db.deleteAllRecord()
# db.delete_old_Record(30) Удалить записи старше 30 дней

#  4 запрос: # востановление из _checkStaff
# restoreFromBackup()

# Отметить запись как выгруженную
# db.change_unload_status(record_id, value=0) record_id : идентификатор, value:флаг выгрузки


import sqlite3
import datetime
import time,comPort_utils


class db():
    def __init__(self, baseName):
        # или :memory: чтобы сохранить в RAM
        self.conn = sqlite3.connect(baseName)
        self.cursor = self.conn.cursor()
        self.creatTable()

    def creatTable(self):
        try:
            # Создание таблицы
            self.cursor.execute("""
            CREATE TABLE "staffWork" (
            "test_id_int"	INTEGER NOT NULL DEFAULT 1 PRIMARY KEY AUTOINCREMENT,
            "propusk_id_txt"	TEXT NOT NULL,            
            "DateTime"	TEXT,            
            "export_bl"	INTEGER,
            "workPlace_int"	INTEGER);
            """)
            print('sql : create')
        except:
            print('sql : use')

    def regPropusk(self, propusk_id_txt, workPlace_int):
        if propusk_id_txt == '':
            print("регистрация пустого номера отмена")
            return
        command = """
        INSERT INTO "main"."staffWork"(
                    "propusk_id_txt"    ,"export_bl"    ,"DateTime"     ,"workPlace_int") 
            VALUES ('%propusk_id_txt%'  ,'%export_bl%'  ,'%DateTime%'   ,'%workPlace_int%');
        """
        command = command.replace('%propusk_id_txt%', comPort_utils.removeFix(propusk_id_txt))
        command = command.replace('%DateTime%', str(datetime.datetime.today()))
        command = command.replace('%export_bl%', str(0))
        command = command.replace('%workPlace_int%', str(workPlace_int))

        self.cursor.execute(command)
        # Сохраняем изменения
        self.conn.commit()

    # Sample:
    # sql     = "SELECT * FROM 'checkStaff'"
    # result  = db.sqlQuery_fetch(sqlQuery=sql)
    # см: Запрос с именованными заполнителями
    def sqlQuery_fetch(self, sqlQuery, param):
        if param == None:
            self.cursor.execute(sqlQuery)
        else:
            self.cursor.execute(sqlQuery, param)

        return self.cursor.fetchall()

    def change_unload_status(self, record_id, value=0):
        command = """
        UPDATE "main"."staffWork" SET "export_bl"=:value WHERE "test_id_int"=:id;
        """
        self.cursor.execute(command, {'value':value,'id':record_id})
        # Сохраняем изменения
        self.conn.commit()

    def deleteAllRecord(self):
        command = """
        DELETE FROM "main"."staffWork";
        """
        self.cursor.execute(command)
        # Сохраняем изменения
        self.conn.commit()

    def delete_old_Record(self, days_old=15):
        command = """
        DELETE     
        FROM staffWork     
        WHERE
        CAST((julianday('now') - julianday(DateTime) ) as integer) >:daysOld
        and export_bl<>0;
        """
        self.cursor.execute(command, {'daysOld': days_old})
        # Сохраняем изменения
        self.conn.commit()



# creatTable()
if __name__ == "__main__":
    print('exit ok')
