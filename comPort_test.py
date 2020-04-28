import comPort_Sql,comPort_utils

# 1
# cursor     =   comPort_Sql.returnCursor()
# comPort_Sql.creatTable(cursor)

db  =   comPort_Sql.db()

# 2
sql     = "SELECT * FROM 'checkStaff'"
result  = db.sqlQuery_fetch(sqlQuery=sql)
for target_list in result:    
    print(target_list)
    mPropusk    =   comPort_utils.removeFix(target_list[0])
    print(mPropusk)    
    db.regPropusk(mPropusk,0)
