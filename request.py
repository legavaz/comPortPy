import requests 
url     =   'http://1c-www-server/Buh-L-PACK/hs/numenkl/nom/'
param   =   '1872,7472'
user    =   '1cv8'
password=   ''
req     = requests.get(url+param, auth=(user,password))  

print(req.url)

if req.status_code==200:
    print(req.text)
else:
    print('ошибка подключения',req.status_code)


