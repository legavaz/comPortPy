
import configparser,os

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
        self.setting    =   {
                            'port':self.port,
                            'baudrate':self.baudrate,
                            'timeout':self.timeout,
                            'db':self.db,
                            'stanok':self.stanok
                            }

    def print_setting(self):
        print(self.setting)





 