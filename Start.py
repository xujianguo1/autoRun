from conf import Config #配置必须先引入，自执行，加载log配置
import uiautomator2 as u2
import time
from app.settingAPK import SettingAPK
from app.dfcfAPK import DfcfAPK
from app.zsyhAPK import ZsyhAPK
from myutil.OpDesc import OpMenu

from app.yhzq.InnerFund import InnerFund

dfcfConfigFile="resources/dfcf.yml"
yhzqConfigFile="resources/yhzq.yml"
yjbConfigFile="resources/yjb.yml"
zsyhConfigFile="resources/zsyh.yml"

def connectPhone():
    opStr=input("请输入机器名或者IP（1：机器名，2：IP）：")
    if opStr=="1" :
        machineName = input("请输入机器名,1为默认[8UR4C19C07001524]：")
        if machineName=="1":
            machineName="8UR4C19C07001524"
        adb = u2.connect(machineName)
    else:
        ipAddress = input("请输入要连接的机器IP：")
        adb= u2.connect_wifi(ipAddress)
    return adb



#东方财富申购新股测试
def dfcfApplyNewStock():
    adb=connectPhone()
    dfcfApp = DfcfAPK(adb)
    dfcfApp.stop()
    dfcfApp.start()
    dfcfApp.applyNewStock()
    


#东方财富申购新债
def dfcfApplyNewCB(adb):
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

def zsyhDaily(adb):
    #zsConfig= Config.loadConfig(zsyhConfigFile)
    zsyhApk= ZsyhAPK(adb)
    zsyhApk.start()
    time.sleep(5)
    zsyhApk.login("13103245")
    zsyhApk.bwjlPlan("路过","123456")
    time.sleep(10)
   # zsyhApk.stop()

def yhzqApplyInnerFund(adb):

    yhzqInnerFund=InnerFund(adb)
    yhzqInnerFund.run()

def mainFlow():
    adb=connectPhone()
    settingAPK = SettingAPK(adb)
    #settingAPK.modifySleeptime() #获取and 设置休眠时间

    menu=initModules() #初始化模块信息
    args=(adb)
    menu.showMenuAndRun(args)
    #zsyhDaily(adb)
    #任务结束，恢复休眠时间
    #settingAPK.resetSleepTime()
    settingAPK.stop()


    


def initModules():
    opMenu =OpMenu()
    opMenu.addItem(1,"东方财富可转债申购",dfcfApplyNewCB)
    opMenu.addItem(2,"银河证券场内基金申购(需手动登录)",yhzqApplyInnerFund)
    return opMenu

if (__name__=="__main__"):
    #testSetSleepTime()
    #dfcfApplyNewStock()
    #dfcfApplyNewCB()
    mainFlow()
    


