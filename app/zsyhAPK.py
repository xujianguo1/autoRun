from app.baseAPK import APK
import uiautomator2 as u2
import logging
import time
import random

class ZsyhAPK(APK):
    logger = logging.getLogger(__name__)
    pathInfo={
        'homePage':'//*[@resource-id="cmb.pb:id/tab"]/android.widget.LinearLayout[1]',
        'comment':'//*[@resource-id="cmb.pb:id/tab"]/android.widget.LinearLayout[2]',
        'licai':'//*[@resource-id="cmb.pb:id/tab"]/android.widget.LinearLayout[3]',
        'life':'//*[@resource-id="cmb.pb:id/tab"]/android.widget.LinearLayout[4]',
        'my':'//*[@resource-id="cmb.pb:id/tab"]/android.widget.LinearLayout[5]',
        }
    def __init__(self,adb):
        self.__adb=adb
        super().__init__(adb,"招商银行","cmb.pb")
    
    def login(self,pwd):
        self.logger.info(self.__str__()+"，准备登陆了。")
        self.goTab(self.pathInfo.get("my")) #点击我的
        time.sleep(1)
        self.checkExistsAndClick("com.android.systemui:id/button2") #弹出指纹登录，点击取消
        self.waitAndClickByResId("cmb.pb:id/btnMore",5) #点击更多
        self.waitAndClickByResId("cmb.pb:id/tvOption",5,"密码登录") #点击密码登录
        self.__inputPwd("cmb.pb:id/editPassword",pwd) #输入密码 输入密码很特殊
        self.waitAndClickByResId("cmb.pb:id/vLoginButtonArea",5)   #点击登录

        time.sleep(10) #休息10秒
        if(self.__adb(resourceId="cmb.pb:id/userName_textView").exists):
            self.logger.info("登录成功，显示登录用户名："+self.__adb(resourceId="cmb.pb:id/userName_textView").get_text())
            return  True
        else:
            self.logger.info("登录失败,请检查参数等信息。。。。！！！！")
            return  False

    def __inputPwd(self,resId,pwd):
        self.logger.info("我要输入密码了。。")    
        self.checkExistsAndClick(resId)
        id_shift="cmb.pb:id/nkb_qwerty_btn_shift" #abc->ABC
        id_abc="cmb.pb:id/nkb_number_btn_qwerty"  #123->abc
        id_123="cmb.pb:id/nkb_qwerty_btn_number"  #abc->123
        idPrefix="xx"
       # id_symbol="cmb.pb:id/nkb_qwerty_btn_symbol" #abc->symbol    ,还有symbol->123 ,symbol->abc(ABC) 没实现
        oldType="1" #1数字，2：小写字母，3，大写字母  12，13，23，32，31，
        cur="0"
        for c in str(pwd) :
            num=ord(c)
            self.logger.debug( "字符[%s]识别的类型为[%s]" % (c,num))
            if(num>=48 and num<= 57): #123
                cur="1"
                idPrefix="cmb.pb:id/nkb_number_btn_"
            elif (num>=97 and num<= 122): #abc
                cur="2"
                idPrefix="cmb.pb:id/nkb_qwerty_btn_"
            elif (num>=65 and num<= 90): #ABC
                num=num+32 #变换为小写操作
                cur="3"
                idPrefix="cmb.pb:id/nkb_qwerty_btn_"
            #特殊字符，暂时未实现，后续再处理    
            else:   
                self.logger.error("密码里面有无法识别的字符："+str(c))

            if(oldType==cur):
                self.checkExistsAndClick(idPrefix+str(num)) 
            else:
                opStr=oldType+cur
                if(opStr=="12"):
                    self.checkExistsAndClick(id_abc) #点击 ABC切换键盘
                elif(opStr=="13"):
                    self.checkExistsAndClick(id_abc) #点击 ABC切换键盘
                    self.checkExistsAndClick(id_shift) #点击shift
                elif(opStr=="23"):
                    self.checkExistsAndClick(id_shift) #点击shift
                elif(opStr=="21"): 
                    self.checkExistsAndClick(id_123)
                elif(opStr=="32"):
                    self.checkExistsAndClick(id_shift) #点击shift
                elif(opStr=="31"):      
                    self.checkExistsAndClick(id_123)
                else:
                    self.logger.error("无法识别的类型："+opStr)
                oldType=cur
                cur="0"    
                self.checkExistsAndClick(idPrefix+str(num)) #点击字符    

        self.logger.info("密码输入完成！。。，准备点击登录")        




    def goTab(self,tapPath):
        self.logger.debug("将要点击tap,xpath="+tapPath)
        self.__adb.xpath(tapPath).click()

    #登录成功后进行任务
    def bwjlPlan(self,wxName,qqName):
        self.goTab(self.pathInfo.get("comment"))
        time.sleep(5)
        self.__adb(text="推荐").long_click()
        opResult={"read":0,"share":0,"comment":0,"focus":0} #操作结果
        for i in range(10): #5篇文章
            j=0
            while(j<5):
                step=random.randrange(10,150)
                #self.__adb(scrollable=True).scroll(steps=step)
                self.__adb.touch.down(600,600)
                self.__adb.touch.move(150, 0)
                self.logger.info("准备第%s次点击了 " % j)
                self.__adb.click(0.271+0.1*i, 0.474+0.05*i) #随机点中间
                time.sleep(i+random.randrange(5,10))  #随眠段时间
                j=j+1
                if(self.__adb(text="写下你的精彩评论").exists):
                    break  #跳到详情页就跳出循环
            
            startTime= int(time.time())
            self.logger.info("准备滑动距离1..")
            self.__adb(scrollable=True).scroll(steps=150) #滑动一定距离
            time.sleep(random.randrange(15,25))
            self.logger.info("睡眠结束，准备持续滑动距离 。。。")
            self.__adb(scrollable=True).scroll.to(text="全部评论")
            time.sleep(2)
            self.__adb(scrollable=True).scroll(steps=200)
            endTime=int(time.time())

            needTime = abs(60-(endTime-startTime))
            self.logger.info("需要睡眠基础时间："+str(needTime))
            time.sleep(random.randrange(needTime,needTime+10)) #随眠一段时间

            if(opResult.get("focus")<1): #没关注，关注一把
                self.logger.info("要进行关注了。。。")
                if(self.__adb(text="关注").exists):
                    self.__adb(text="关注").click() #关注了
                    opResult["focus"]=opResult.get("focus")+1
                    self.logger.info("关注成功！")
            time.sleep(random.randrange(2,5))
            if(opResult.get("comment")<2):    
                self.logger.info("要进行评论了。。。")
                self.__adb(text="写下你的精彩评论").click()
                time.sleep(random.randrange(3))
                self.__adb(className="android.widget.EditText").set_text('路过打一下卡') #输入评论
                time.sleep(random.randrange(4))
                self.__adb(text="发布").click()  #发布按钮
                opResult["comment"]=opResult.get("comment")+1  #设置评论+1
                self.logger.info("完成评论了。。。")

            time.sleep(random.randrange(2,5))  

            if(opResult.get("share")<2):  
                if( random.randrange(1,10)%2==0):  #qq与微信随机
                    self.logger.info("准备开始进行分享了。。。。。")
                    self.__adb.click(0.915, 0.971)    #点击分享
                    time.sleep(1)
                    self.__adb(text="微信好友").click() #微信好友
                    self.shareToWx(wxName)
                    self.logger.info("微信分享完成了，已经返回招行了。。。。。。")
                else:
                    time.sleep(random.randrange(2,5))
                    self.logger.info("准备开始进行qq分享了。。。。。")
                    self.__adb.click(0.915, 0.971)    #点击分享
                    time.sleep(1)
                    self.__adb(text="QQ").click() 
                    self.shareToQQ(qqName) 
                    self.logger.info("QQ分享完成了，已经返回招行了。。。。。。")
                opResult["share"]=opResult.get("share")+1      #分享次数+1
            opResult["read"]=opResult.get("read")+1  
            self.logger.info("一篇文章处理完成。。")
            self.pressBack()