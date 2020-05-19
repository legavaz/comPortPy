import comPort_Sql,comPort_utils

db      =   comPort_Sql.db('checkStaff.db')

def restoreFromBackup():    
    # Перенос записей из старой таблицы
    dbOld   =   comPort_Sql.db('_checkStaff.db')
    sql     = "SELECT * FROM 'checkStaff' ;"
    result  =   dbOld.sqlQuery_fetch(sql,None)
    for target_list in result:    
        # Перенос из старой базы данных
        # {
        mPropusk    =   comPort_utils.removeFix(target_list[0])        
        db.regPropusk(mPropusk,10) #Регистрация в базе данных
        # }
        print(target_list)
        
setting = comPort_utils.setting()

setting.print_setting()

db.deleteAllRecord()







