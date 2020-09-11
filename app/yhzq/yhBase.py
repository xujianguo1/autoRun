from app.baseAPK import APK
from app.viewUtil import ListView
import uiautomator2 as u2
import logging
import time
import random

class YhBase(APK):
    logger = logging.getLogger(__name__)
    def __init__(self,adb):
        self.__adb=adb
        #self.initKeyBoard()
        super().__init__(adb,"银河证券场操作","yhzq.YhBase")
        super().setStartAndStop(False,False)
        

    #键盘操作暂时不用，先看看简单的
    def initKeyBoard(self):
        return  0
