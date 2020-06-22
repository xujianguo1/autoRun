from app.baseAPK import APK
import uiautomator2 as u2
import logging
import time

#定义东方财富apk
class DfcfAPK(APK):
    logger = logging.getLogger(__name__)
    def __init__(self,adb):
        self.__adb=adb
        super().__init__(adb,"东方财富","com.eastmoney.android.berlin")

   
     
    def login(self,account,pwd):
        #time.sleep(10) #等待10秒，有的启动的时候，第一次启动，可能会有广告
        self.logger.debug("准备点击交易")
        self.__adb(resourceId="com.eastmoney.android.berlin:id/btn5").wait(timeout=10) #点击交易
        self.__adb(resourceId="com.eastmoney.android.berlin:id/btn5").click() 
        self.logger.debug("准备点击登录")
        self.__adb(resourceId="com.eastmoney.android.berlin:id/note").wait(timeout=5)
        self.__adb(resourceId="com.eastmoney.android.berlin:id/note").click() #点击登录
        self.logger.debug("准备点击 传统登录")
        self.__adb(resourceId="com.eastmoney.android.berlin:id/tradition_login").wait(timeout=5)
        self.__adb(resourceId="com.eastmoney.android.berlin:id/tradition_login").click() #点击传统登录  代替 adb(text="传统登录").click()
        self.logger.debug("准备输入账户与密码 并登录")
        self.__adb(resourceId="com.eastmoney.android.berlin:id/trade_login_btn").wait(timeout=5)
        self.__adb(resourceId="com.eastmoney.android.berlin:id/account_tv").set_text(account) #输入账号
        self.__adb(resourceId="com.eastmoney.android.berlin:id/password_tv").set_text(pwd) #密码
        self.__adb(resourceId="com.eastmoney.android.berlin:id/trade_login_btn").click() #登录
        self.logger.debug("登录成功了。。。account="+str(account))
        time.sleep(5)
        if( self.__adb.exists(resourceId="com.eastmoney.android.berlin:id/right_close")):
            self.logger.debug("login 后，有弹窗,需要关闭")
            self.__adb(resourceId="com.eastmoney.android.berlin:id/right_close").click()
        text= self.__adb(resourceId="com.eastmoney.android.berlin:id/username").get_text()
        if(len(text)>5):
            self.logger.info("登录成功，账户信息："+text)
            return True
        else:
            return False       
        
    def applyNewStock(self):
        loginResult=self.login("540300278672","131032")
        self.logger.info("登录完成。。")
        if( not loginResult):
            self.logger.error("！！！！！登录失败，请检查！！！！！！！！！！")
            return loginResult
        #开始执行申购新股
        self.logger.info("开始执行 新股申购。。。")

    def applyNewCB(self,account,pwd):
        loginResult=self.login(account,pwd)
        self.logger.info("登录完成。。")
        if( not loginResult):
            self.logger.error("！！！！！登录失败，请检查！！！！！！！！！！")
            return loginResult
        #开始执行申购新股
        self.logger.info("开始执行 新债申购。。。")

        self.__adb(resourceId="com.eastmoney.android.berlin:id/text1", text="新债申购").click_exists(timeout=5)
        time.sleep(5)
        self.logger.debug("点击申购成功，开始检查是否有新债。。")
        noCB=self.__adb(text="暂无新债可申购").exists
        if(noCB):
            self.logger.warn("今天没有新债，程序会退出申购")
            return None

        self.logger.info("有新债申购，开始一键全部申购。。")








  
if (__name__ =="__main__"):
    machineName='8UR4C19C07001524'
    adb = u2.connect(machineName)   
    adb.press('home')
    dfcfApk=DfcfAPK(adb)
    dfcfApk.applyNewStock()


    
