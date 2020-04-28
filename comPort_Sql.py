import sqlite3,time


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
            "export_bl"	INTEGER,
            "workPlace_int"	INTEGER);
            """)
            print('sql : ok')
        except:
            print('sql : use')
    
    def regPropusk(self,propusk_id_txt,workPlace_int):
        command =   """
        INSERT INTO "main"."staffWork"(
            "propusk_id_txt","time_int","time_str","export_bl","workPlace_int") 
            VALUES ('%propusk_id_txt%','%time_int%','%time_str%','%export_bl%','%workPlace_int%');
        """
        command =command.replace('%propusk_id_txt%'  ,propusk_id_txt)
        command =command.replace('%time_int%'        ,str(time.time()))
        command =command.replace('%time_str%'        ,time.strftime('%H:%M:%S'))
        command =command.replace('%export_bl%'       ,str(0))
        command =command.replace('%workPlace_int%'   ,str(workPlace_int))

        self.cursor.execute(command)
        # Сохраняем изменения
        self.conn.commit()

    def sqlQuery_fetch(self, sqlQuery):
        self.cursor.execute(sqlQuery)
        return self.cursor.fetchall()


# creatTable()
if __name__ == "__main__":
    print ('exit ok')
