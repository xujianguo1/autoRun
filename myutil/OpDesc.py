#操作项
class OpItem(object):
    def __init__(self,opStr,opDesc,runMethod):
        self.__opStr= str(opStr)
        self.__opDesc= opDesc
        self.__runMethod= runMethod   

    def getItemDesc(self):
        return  str(self.__opStr)+"  : "+self.__opDesc  

    def isOpStr(self,opStr):
        if self.__opStr== opStr:
            return True
    def getOpFunc(self):
        return self.__runMethod

class OpMenu(object):
    def __init__(self):
        self.__opItemList=[]   

    #添加一个项目
    def addItem(self,opStr,opDesc,opFunc):
        self.__opItemList.append(OpItem(opStr,opDesc,opFunc))   

    def showMenuAndRun(self,*arg):
        #isExit=False
        isContinue = True
        while isContinue :
            self.showMenu()
            rs =self.getChooseItem()
            if rs == -1:
                isContinue=False
                #isExit=True
            elif rs==0:
                 print("输入选择错误，请正确选择！！！")
                 isContinue=True
            else:
                try:
                    rs(*arg)
                except BaseException as err:
                    print("出现异常：",err)

    #打印菜单
    def showMenu(self):
        print("请选择要执行的操作(-1退出)：")
        for op in self.__opItemList :
            item= op.getItemDesc()
            print("    "+item)
        print("  -1  :  退出菜单")    

    #获取输入& 运行，-1为返回，0为继续，其他则执行
    def getChooseItem(self):
        opStr=input()
        if opStr=="-1" :
            return -1
        for item in self.__opItemList:
            if item.isOpStr(opStr):
                return item.getOpFunc()
        return 0        