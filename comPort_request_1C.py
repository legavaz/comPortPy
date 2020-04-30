
import requests,json
import comPort_Sql,comPort_utils

# Чтение настроек из файла ini
setting = comPort_utils.setting()
setting.print_setting()

# подключаем базу данных
db      =   comPort_Sql.db(setting.db)

def list_json_for_1C():
    # *******1 запрос: Выборка для выгрузки в 1С со статусом: ({'export_bl':0})
    sql  = """
        SELECT test_id_int,
            propusk_id_txt,
            DateTime,
            workPlace_int 
        FROM 'staffWork' 
        WHERE export_bl=:export_bl;
        """
    result  =   db.sqlQuery_fetch(sql,{'export_bl':0})
    # обход результата запроса
    mList   =   []
    for target_list in result:    
        param = {
            'test_id_int': target_list[0],
            'propusk_id_txt': target_list[1],
            'DateTime': target_list[2],            
            'workPlace_int': target_list[3]}
        mList.append(param)
    return json.dumps(mList)

def change_status(json_str):
    mlist   =   json.loads(json_str)
    for target_list in mlist:
        db.change_unload_status(target_list['test_id_int'],1)
        # print(target_list)

param   =   list_json_for_1C()

if json.loads(param)    !=  []:
    # выгрузка в 1С get методом
    req = requests.get(setting.url_http_service+param, auth=(setting.user, setting.password))

    if req.status_code == 200:
        print(req.text)
        change_status(param)
    else:
        print('ошибка подключения', req.status_code)
else:
    print('нет данных для выгрузки')
