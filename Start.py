import conf.Config #配置必须先引入，自执行，加载log配置
import uiautomator2 as u2
import time
from app.settingAPK import SettingAPK
def connectPhone():
    machineName='8UR4C19C07001524'
    adb = u2.connect(machineName)
    return adb

def test():
    adb=connectPhone()
    settingAPK = SettingAPK(adb)
    settingAPK.start()
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





if (__name__=="__main__"):
   test()