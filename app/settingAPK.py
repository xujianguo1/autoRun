from app.baseAPK import APK
from app.viewUtil import ListView
import logging
class SettingAPK(APK):
    logger = logging.getLogger(__name__)
    def __init__(self,d):
        self.__adb = d
        super().__init__(d,"设置","com.android.settings",".HWSettings")

    def getSleepInfo(self):
        self.__adb(resourceId="android:id/title", text="显示和亮度").click()
        self.__adb(text="休眠").click()
        targetList=self.__adb(resourceId="android:id/select_dialog_listview").child(className="android.widget.CheckedTextView")
        listView = ListView(targetList,"休眠时间","设置里面显示与亮度")
        selected= listView.getSelectedValue()
        maxValue= listView.getLastValue()
        self.logger.debug("设置获取休眠值：[%s] ,得到最大值：[%s]" % (selected,maxValue))
        return [selected,maxValue]

    def setSleepInfo(self,targetText):
        self.__adb(resourceId="android:id/title", text="显示和亮度").click()
        self.__adb(text="休眠").click()
        targetList=self.__adb(resourceId="android:id/select_dialog_listview").child(className="android.widget.CheckedTextView")
        listView = ListView(targetList,"休眠时间","设置里面显示与亮度")
        result= listView.doSelect(targetText)
        self.logger.debug("设置获取休眠值：%s , 操作结果：%s" % (targetText,result))
        return result

