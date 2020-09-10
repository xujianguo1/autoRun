from app.baseAPK import APK
from app.viewUtil import ListView
import logging
class SettingAPK(APK):
    logger = logging.getLogger(__name__)
    def __init__(self,d):
        self.__adb = d
        super().__init__(d,"设置","com.android.settings",".HWSettings")

    def getSleepInfo(self):
        self.__showSetting()
        targetList=self.__adb(resourceId="android:id/select_dialog_listview").child(className="android.widget.CheckedTextView")
        listView = ListView(targetList,"休眠时间","设置里面显示与亮度")
        selected= listView.getSelectedValue()
        maxValue= listView.getLastValue()
        self.logger.debug("设置获取休眠值：[%s] ,得到最大值：[%s]" % (selected,maxValue))
        return [selected,maxValue]

    def __showSetting(self):
        self.waitAndClickByResId("android:id/title", 5,"显示和亮度")
        self.waitAndClickByText("休眠")

    def __setSleepInfo(self,targetText):
        
        targetList=self.__adb(resourceId="android:id/select_dialog_listview").child(className="android.widget.CheckedTextView")
        listView = ListView(targetList,"休眠时间","设置里面显示与亮度")
        result= listView.doSelect(targetText)
        self.logger.debug("设置获取休眠值：%s , 操作结果：%s" % (targetText,result))
        return result

    #调整睡眠时间到最后一项
    def modifySleeptime(self):
        self.start()
        values = self.getSleepInfo()
        cur = values[0]
        max = values[1]
        self.logger.info("设置获取到的值：cur=%s ,max= %s" % (cur,max))
        self.__orginal=cur
        self.__setSleepInfo(max)
        self.stop()
        return cur

    #恢复睡眠时间到原始值
    def resetSleepTime(self):
        self.start()
        self.logger.info("恢复睡眠时间为："+self.__orginal)
        self.__showSetting()
        self.__setSleepInfo(self.__orginal)
        self.stop()
