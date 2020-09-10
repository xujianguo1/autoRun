from app.constant import OP_KEY 
class APK:
    def __init__(self,adb,aliasName,packageName,acitvityName=None):
        self.__adb = adb
        self.__packageName = packageName
        self.__aliasName= aliasName
        self.__activityName=acitvityName
        self.setStartAndStop(True,True)

    def start(self):
        if not(self.__isCanStart):
            print("不允许进行： 启动操作")
            return 
        self.stop()#先停止一次，让回到原始状态
        self.__adb.press(OP_KEY.HOME)
        if(self.__activityName == None):
            self.__adb.app_start(self.__packageName)
        else:
            self.__adb.app_start(self.__packageName,activity=self.__activityName)
        print("start application ,name=[%s],package=[%s]" % (self.__aliasName,self.__packageName))    
        
    def stop(self):
        if not(self.__isCanStop):
            print("不允许进行： 停止操作")
            return 
        self.__adb.app_stop(self.__packageName)
        self.__adb.press(OP_KEY.HOME)      

    ##设置是否可以启动、停止（有的只是半自动化（界面操作），这2个动作不能执行）
    def setStartAndStop(self,isCanStart,isCanStop):
        self.__isCanStart = isCanStart
        self.__isCanStop = isCanStop    

    #点击返回上一级
    def pressBack(self): 
        self.__adb.press(OP_KEY.BACK)

    #等待一定的时间，出现就点击
    def __waitAndClick(self,resId,timeout):
        self.__adb(resourceId=resId).wait(timeout)
        self.__adb(resourceId=resId).click()    

    #等待一定的时间，出现就点击
    def waitAndClickByResId(self,resId,timeout=5,txt=None):
        if(txt==None):
            self.__waitAndClick(resId,timeout)
        else:
            self.__adb(resourceId=resId,text=txt).wait(timeout)
            self.__adb(resourceId=resId,text=txt).click()  

    #检查text是否存在，并且点击 ，检查时间默认5秒
    def waitAndClickByText(self,txt,timeout=5):
        self.__adb.wait_timeout=3   #默认必须等待1S
        self.__adb(text=txt).wait(timeout)
        self.__adb(text=txt).click()

    def getResourceAndInput(self,resId,inputText):
        self.__adb(resourceId=resId).wait(5) #默认等待5s
        self.__adb(resourceId=resId).set_text(inputText)

    #检查resId组价是否存在，存在就点击
    def checkExistsAndClick(self,resId):    
        if(self.__adb(resourceId=resId).exists):
            self.__adb(resourceId=resId).click()
        else:
            print("目标不存在，无法点击！！！！！！！！！id="+resId)

    def shareToWx(self,wxName):
        self.waitAndClickByResId("com.tencent.mm:id/c55")
        self.__adb(resourceId="com.tencent.mm:id/bhn").set_text(wxName)
        self.waitAndClickByResId("com.tencent.mm:id/gbv",5,wxName)
        self.waitAndClickByResId("com.tencent.mm:id/doz")
        self.waitAndClickByResId("com.tencent.mm:id/dom")   

    def shareToQQ(self,qqName):
        self.waitAndClickByResId("com.tencent.mobileqq:id/et_search_keyword")
        self.__adb(resourceId="com.tencent.mobileqq:id/et_search_keyword").set_text(qqName)
        self.waitAndClickByResId("com.tencent.mobileqq:id/title", 5,qqName)
        self.waitAndClickByResId("com.tencent.mobileqq:id/dialogRightBtn")
        self.waitAndClickByResId("com.tencent.mobileqq:id/dialogLeftBtn")     

    def __str__(self):
        return 'APK [ name=%s ,packageName=%s ,activityName=%s]' % (self.__aliasName,self.__packageName,self.__activityName)

