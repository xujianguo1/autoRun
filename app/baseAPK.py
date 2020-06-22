from app.constant import OP_KEY 
class APK:
    def __init__(self,adb,aliasName,packageName,acitvityName=None):
        self.__adb = adb
        self.__packageName = packageName
        self.__aliasName= aliasName
        self.__activityName=acitvityName

    def start(self):
        self.stop()#先停止一次，让回到原始状态
        self.__adb.press(OP_KEY.HOME)
        if(self.__activityName == None):
            self.__adb.app_start(self.__packageName)
        else:
            self.__adb.app_start(self.__packageName,activity=self.__activityName)
        print("start application ,name=[%s],package=[%s]" % (self.__aliasName,self.__packageName))    
        
    def stop(self):
        self.__adb.app_stop(self.__packageName)
        self.__adb.press(OP_KEY.HOME)      

    #点击返回上一级
    def pressBack(self): 
        self.__adb.press(OP_KEY.BACK)


    def __str__(self):
        return 'APK [ name=%s ,packageName=%s ,activityName=%s]' % (self.__aliasName,self.__packageName,self.__activityName)

