import requests
import sqlite3
import json

# Параметры подключения к 1С
url = 'http://localhost/danv_copy_lpack_buh3/hs/staffstatis/import/'
param = '1872_python'
user = '1cv8'
password = ''


# Параметры подключения к временной базе
conn = sqlite3.connect("checkStaff.db")  # или :memory: чтобы сохранить в RAM
cursor = conn.cursor()


def cleanStr(strIn):
    goodLetter = '0123456789.'
    result = ''
    for let in strIn:
        for blet in goodLetter:
            if let == blet:
                result += let

    return result


sql = "SELECT * FROM 'checkStaff'"
cursor.execute(sql)
result = cursor.fetchall()
mList = []

for target_list in result:    
    param = {'propusk': cleanStr(target_list[0]),
             'time': target_list[1],
             'timeInt': target_list[2]}
    mList.append(param)

param = json.dumps(mList)
# print(param)
req = requests.get(url+param, auth=(user, password))
if req.status_code == 200:
    print(req.text)
else:
    print('ошибка подключения', req.status_code)

