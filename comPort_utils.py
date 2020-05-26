
import configparser,os,time


def exit_program(msg_str:str=''):
    if msg_str.strip(' ')=='':
        print('exit...')
    else:
        print('exit...',msg_str)
    time.sleep(3)


def removeFix(mString=""):
    goodLetter = '0123456789'
    result = ''
    for let in mString:
        for blet in goodLetter:
            if let == blet:
                result += let

    return result

class setting():
    def __init__(self):        
        self.path       =  "comPort_setting.ini"
        self.setting    =   {}        
        self.readConfig()    

    def createConfig(self):
        """
        Create a config file
        """
        config = configparser.ConfigParser()
        config.add_section("DEVICE")
        config.set("DEVICE", "port", "com7")
        config.set("DEVICE", "baudrate", '9600')
        config.set("DEVICE", "timeout", '1')
        
        config.add_section("DB")
        config.set("DB", "db", "checkStaff.db")

        config.add_section("MACHINE")
        config.set("MACHINE", "stanok", '77')

        config.add_section("CONNECT_1C")
        config.set("CONNECT_1C", "url_http_service" , 'http://1c-www-server/erp/hs/staffstatis/import/')
        config.set("CONNECT_1C", "user"             , '1cv8')
        config.set("CONNECT_1C", "password"         , '')


        with open(self.path, "w") as config_file:
            config.write(config_file)

    def readConfig(self):      
        
        if not os.path.exists(self.path):        
            self.createConfig()
        
        config = configparser.ConfigParser()
        config.read(self.path)

        self.port       =   config.get("DEVICE", "port")
        self.baudrate   =   config.get("DEVICE", "baudrate")
        self.timeout    =   config.get("DEVICE", "timeout")

        self.db         =   config.get("DB", "db")        
        self.stanok     =   config.get("MACHINE", "stanok")

        self.url_http_service   =   config.get("CONNECT_1C", "url_http_service")        
        self.user               =   config.get("CONNECT_1C", "user")
        self.password           =   config.get("CONNECT_1C", "password")

        self.setting    =   {
                            'port':self.port,
                            'baudrate':self.baudrate,
                            'timeout':self.timeout,
                            'db':self.db,
                            'stanok':self.stanok,
                            'url_http_service':self.url_http_service,
                            'user':self.user,                            
                            'password':self.password
                            }

    def print_setting(self):
        print(self.setting)





 