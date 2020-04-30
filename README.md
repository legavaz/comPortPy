# comPortPy (сбор информации о времени регистрации магн.карт и передача в 1с)

(КЛИЕНТ)

comPort_scaner.py - сценарий сканирования магнитных карт, (подразумевается постоянно запущенная работа на клиенте)

comPort_request_1C.py - сценарий для выгрузки в 1с (метод get) (запуск по расписанию, для выгрузки в БД, при успешном событии, записать отметку о выгрузке)

(СЕРВЕР - 1С)

Р_http_import.cfe - Расширение для приема сообщений, основной пакет хранения реализован на регистре сведений (Расш1_ПакетЗагрузки)


Дополнительные модули и объекты:

  comPort_Sql.py (работа с SQLite)   
  comPort_utils.py (работа с настройками и пр.)
