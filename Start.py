from conf import Config #配置必须先引入，自执行，加载log配置
import uiautomator2 as u2
import time
from app.settingAPK import SettingAPK
from app.dfcfAPK import DfcfAPK

dfcfConfigFile="resources/dfcf.yml"
yhzqConfigFile="resources/yhzq.yml"
yjbConfigFile="resources/yjb.yml"

def connectPhone():
    #machineName='8UR4C19C07001524'
    #adb = u2.connect(machineName)
    ipAddress = "10.242.139.99"
    adb= u2.connect_wifi(ipAddress)
    return adb



def testSetSleepTime():
    adb=connectPhone()
    settingAPK = SettingAPK(adb)
    settingAPK.modifySleeptime()
    values = settingAPK.getSleepInfo()
    cur = values[0]
    max = values[1]
    print("获取到的值：cur=%s ,max= %s" % (cur,max))
    settingAPK.stop()
    time.sleep(6)

    print("我已经休眠了60.。。 要设置最大值了。。")
    settingAPK.start()
    settingAPK.setSleepInfo(max)
    time.sleep(3)
    settingAPK.stop 
    print("最大值已经设置了，我要开始执行相关的任务了。。")


    settingAPK.start()
    settingAPK.setSleepInfo(cur)
    time.sleep(6)

    settingAPK.stop()
    print("全部执行完了")

#东方财富申购新股测试
def dfcfApplyNewStock():
    adb=connectPhone()
    dfcfApp = DfcfAPK(adb)
    dfcfApp.stop()
    dfcfApp.start()
    dfcfApp.applyNewStock()
    


#东方财富申购新债
def dfcfApplyNewCB():
    adb=connectPhone()
    confDict=Config.loadConfig(dfcfConfigFile)
    dfcfApp = DfcfAPK(adb)
    
    defaultPWD=confDict.get("defaultPwd")
    accountList=confDict.get("accountList")
    for acc in accountList :
        account= acc.get("account")
        pwd=acc.get("pwd") or defaultPWD
        dfcfApp.start()
        dfcfApp.applyNewCB(account,pwd)
        dfcfApp.stop()
    print("新债打理完毕")
def mainFlow():
    adb=connectPhone()
    settingAPK = SettingAPK(adb)
    settingAPK.modifySleeptime() #获取and 设置休眠时间

    # 执行其他流程

    
    #任务结束，恢复休眠时间
    settingAPK.resetSleepTime()
    settingAPK.stop()


if (__name__=="__main__"):
    #testSetSleepTime()
    #dfcfApplyNewStock()
    dfcfApplyNewCB()