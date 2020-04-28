import comPort_Sql,comPort_utils
import datetime,time

db      =   comPort_Sql.db('checkStaff.db')
dbOld   =   comPort_Sql.db('_checkStaff.db')

db.deleteAllRecord()

def showQuery(result):    
    if result==None:
        return

    for target_list in result:    
        print(target_list)
        
        # Перенос из старой базы данных
        # {
        mPropusk    =   comPort_utils.removeFix(target_list[0])        
        db.regPropusk(mPropusk,10) #Регистрация в базе данных
        # }
        
        # Отметить запись как выгруженную
        # db.change_unload_status(target_list[0],1) 
        



# *******1 запрос: Выборка для выгрузки в 1С со статусом: ({'export_bl':0}) 
# sql     = "SELECT * FROM 'staffWork' WHERE export_bl=:export_bl;"
# result  =   db.sqlQuery_fetch(sql,{'export_bl':1})

# *******2 запрос: Выборка для удаления старых записей: ({'export_bl':0}) 
# sql     = "SELECT * FROM 'staffWork' WHERE time_int<:start;"
# result  =   db.sqlQuery_fetch(sql,{'start':datetime.datetime.today()})

# print(datetime.datetime.today())
# print(time.time())
# day    =   60*60*24
# mounth =   day*30
# year   =   mounth*12
# print('year',time.time()/year)


# Перенос записей из старой таблицы
sql     = "SELECT * FROM 'checkStaff' ;"
result  =   dbOld.sqlQuery_fetch(sql,None)


showQuery(result)



