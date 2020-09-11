from app.baseAPK import APK
from app.viewUtil import ListView
import uiautomator2 as u2
import logging
import time
import random

#银河证券的场内基金申购
class InnerFund(APK):
    logger = logging.getLogger(__name__)
    def __init__(self,adb):
        self.__adb=adb
        super().__init__(adb,"银河证券场内基金申购","yhzq.innerFund")
        super().setStartAndStop(False,False)

    def run(self):
        print("请输入基金代码、买入账户数量、金额（省略即为全仓） ，例如： 162411 5")
        arg = input("请输入：")
        argStrs=arg.strip().split(" ")

        fundId=argStrs[0]
        accountNum=int(argStrs[1])
        #金额设置
        if len(argStrs)==2 :
            money= None
        else:
            money=argStrs[2]

        #点击场内基金
        self.__adb(scrollable=True).scroll.to(text="场内基金")
        self.waitAndClickByResId("com.galaxy.stock:id/name",5,"场内基金")
        self.waitAndClickByText("基金申购")
        

        for i in range(1,accountNum):
            self.getResourceAndInput("com.galaxy.stock:id/stockCode",fundId)
            accUiList = self.__clickAndShowAccount()
            time.sleep(1)
            accountList = self.__getAllValues(accUiList)
            if i > len(accountList):
                self.logger.info("获取账户长度："+str(len(accountList))+" < "+str(i)+" ,本次不会运行")
                break
            self.__setAccount(accountList[i-1],accUiList)
            time.sleep(1)
            #金额无法数据，点击全仓
            if money==None:
                self.waitAndClickByResId("com.galaxy.stock:id/full")
            else:
                self.getResourceAndInput("com.galaxy.stock:id/inputEt",money)
            #点击申购
            self.waitAndClickByResId("com.galaxy.stock:id/order")

            #第一次接受协议
            time.sleep(6)
            self.waitAndClickByResId("com.galaxy.stock:id/acceptedCb")#同意
            time.sleep(1)
            self.waitAndClickByResId("com.galaxy.stock:id/okBtn") #确定
            
            #接受第二次协议
            time.sleep(2)
            self.waitAndClickByResId("com.galaxy.stock:id/acceptedCb")#同意
            time.sleep(1)
            self.waitAndClickByResId("com.galaxy.stock:id/okBtn") #确定

            #接受第三次协议
            time.sleep(4)
            self.waitAndClickByResId("com.galaxy.stock:id/acceptedCb")#同意
            time.sleep(1)
            self.waitAndClickByResId("com.galaxy.stock:id/okBtn") #确定

            #确认申购(两次)
            time.sleep(1)
            self.waitAndClickByResId("com.galaxy.stock:id/okBtn")
            time.sleep(3)
            result=self.__adb(resourceId="com.galaxy.stock:id/contentTv").info['text']
            print("申购结果："+result)
            self.waitAndClickByResId("com.galaxy.stock:id/okBtn") 

        self.logger.info("本次场内基金申购结束。。具体情况请看日志 or 软件委托单")
        #两次back，回到登录后的主界面
        self.pressBack()    
        self.pressBack() 


    def __clickAndShowAccount(self):
        self.waitAndClickByResId("com.galaxy.stock:id/secuidList")
        tmp =self.__adb(className='android.widget.ListView')
        accUilist=tmp.child(className="android.widget.CheckedTextView")
        return accUilist

    def __getAllValues(self,accUilist):
        listView = ListView(accUilist,"账户列表","银河证券-场内基金申购账户列表")
        accounts = listView.getAllValue()
        return accounts


    def __setAccount(self,accountTxt,accUilist):
        listView = ListView(accUilist,"账户列表","银河证券-场内基金申购账户列表")
        listView.doSelect(accountTxt)
        return 





