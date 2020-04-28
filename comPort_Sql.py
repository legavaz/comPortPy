
# http://unetway.com/tutorial/sqlite/

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


import sqlite3,datetime,time

class db():
    def __init__(self):
        self.conn   =   sqlite3.connect("checkStaff.db")  # или :memory: чтобы сохранить в RAM        
        self.cursor =   self.conn.cursor()
        self.creatTable()

    def creatTable(self):
        # if cursor   ==  None:
        #     cursor  =   returnCursor()
        try:
            # Создание таблицы
            self.cursor.execute("""
            CREATE TABLE "staffWork" (
            "test_id_int"	INTEGER NOT NULL DEFAULT 1 PRIMARY KEY AUTOINCREMENT,
            "propusk_id_txt"	TEXT NOT NULL,
            "time_int"	INTEGER,
            "time_str"	TEXT,
            "DateTime"	timestamp
            "export_bl"	INTEGER,
            "workPlace_int"	INTEGER);
            """)
            # print('sql : ok')
        except:
            print('sql : use')
    
    def regPropusk(self,propusk_id_txt,workPlace_int):
        if propusk_id_txt=='':
            print("регистрация пустого номера отмена")
            return
        command =   """
        INSERT INTO "main"."staffWork"(
            "propusk_id_txt"            ,"time_int"     ,"time_str"     ,"export_bl"    ,"workPlace_int") 
            VALUES ('%propusk_id_txt%'  ,'%time_int%'   ,'%time_str%'   ,'%export_bl%'  ,'%workPlace_int%');
        """
        command =command.replace('%propusk_id_txt%'  ,propusk_id_txt)
        command =command.replace('%time_int%'        ,str(time.time()))
        command =command.replace('%time_str%'        ,str(datetime.datetime.today()))
        command =command.replace('%export_bl%'       ,str(0))
        command =command.replace('%workPlace_int%'   ,str(workPlace_int))

        self.cursor.execute(command)
        # Сохраняем изменения
        self.conn.commit()

    # Sample:
    # sql     = "SELECT * FROM 'checkStaff'"
    # result  = db.sqlQuery_fetch(sqlQuery=sql)
    # см: Запрос с именованными заполнителями
    def sqlQuery_fetch(self, sqlQuery,param):
        if param==None:
            self.cursor.execute(sqlQuery)
        else:
            self.cursor.execute(sqlQuery,param)        
        
        return self.cursor.fetchall()

    def change_unload_status(self,record_id,value=0):        
        command =   """
        UPDATE "main"."staffWork" SET "export_bl"=? WHERE "test_id_int"=?;
        """
        self.cursor.execute(command,value,record_id)
        # Сохраняем изменения
        self.conn.commit()
    
    def deleteAllRecord(self):
        command =   """
        DELETE FROM "main"."staffWork";
        """
        self.cursor.execute(command)
        # Сохраняем изменения
        self.conn.commit()


# creatTable()
if __name__ == "__main__":
    print ('exit ok')
