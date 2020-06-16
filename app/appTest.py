import uiautomator2 as u2
import Constant 
import time
machineName='LKX0218807001731'
d = u2.connect(machineName)

class APK:
    def __init__(self,d,aliasName,packageName,acitvityName=None):
        self.__d = d
        self.__packageName = packageName
        self.__aliasName= aliasName
        self.__activityName=acitvityName

    def start(self):
        self.__d.press(Constant.OP_KEY.HOME)
        if(self.__activityName == None):
            self.__d.app_start(self.__packageName)
        else:
            self.__d.app_start(self.__packageName,activity=self.__activityName)
        print("start application ,name=[%s],package=[%s]" % (self.__aliasName,self.__packageName))    
        
        

    def stop(self):
        self.__d.app_stop(self.__packageName)
        self.__d.press(Constant.OP_KEY.HOME)      

    def __str__(self):
        return 'APK [ name=%s ,packageName=%s ,activityName=%s]' % (self.__aliasName,self.__packageName,self.__activityName)
    
    def getOldValue(self):
        self.start()
        targetList=self.goToItem()
        selectValue=self.getSelectValue(targetList)
        print("find selectText: %s" % selectValue)
        return selectValue

    def resetValue(self,targetText):
        self.start()
        targetList=self.goToItem()
        result= self.selectTargetItem(targetText,targetList)
        return result
        
    def goToItem(self):
        self.__d(resourceId="android:id/title", text="显示和亮度").click()
        self.__d(text="休眠").click()
        targetList=self.__d(resourceId="android:id/select_dialog_listview").child(className="android.widget.CheckedTextView")
        return targetList
    ##获取select的文本
    def getSelectValue(self,targetList):
        for i in range(len(targetList)):
            kv=targetList[i].info
            isChecked=kv["checked"]
            if(isChecked==True ):
                print("findTargetSelect,info=%s" % kv)
                return kv["text"]
    def selectTargetItem(self,text,targetList):
        for i in range(len(targetList)):
            kv=targetList[i].info
            value = kv["text"]
            if(text ==value ):
                print("get Target Obj,text=[%s] ,will be Select： info=%s" % (text,kv))
                targetList[i].click()
                return  True
        return False


class SetingApp(APK):
    def __init__(self,d,aliasName,packageName,acitvityName):
        super().__init__(d,aliasName,packageName,acitvityName)

def testSetting():
    settingAPK=SetingApp(d,"设置","com.android.settings",".HWSettings")
    oldV=settingAPK.getOldValue()
    
   
    settingAPK.resetValue("2 分钟")
    time.sleep(20)
    settingAPK.resetValue(oldV)


#dfcf=APK(d,"com.eastmoney.android.berlin","东方财富")
#print(dfcf)
#dfcf.start()
#time.sleep(15)
#dfcf.stop()


if(__name__ =='__main__'):
    testSetting()
