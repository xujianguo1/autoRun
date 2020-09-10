import logging
class ListView:
    logger = logging.getLogger(__name__)

    def __init__(self,items,listName,desc):
        self.__items = items
        self.__listName= listName
        self.__desc = desc
    def __str__(self):
        return "ListView [name=%s , desc=%s]" % (self.__listName,self.__desc)    
    ##获取select的文本
    def getSelectedValue(self):
        for i in range(len(self.__items)):
            kv=self.__items[i].info
            isChecked=kv["checked"]
            if(isChecked==True ):
                self.logger.debug("findTargetSelect,info=%s" % kv)
                return kv["text"]

    def __getValue(self,index):
        if(index <0):
            index = 0
        if(index >=len(self.__items)):
            index = len(self.__items)-1    
        kv= self.__items[index].info  
        result = kv['text'] 
        return result

    #获取所有的列表值
    def getAllValue(self):
        values=[]
        for item in self.__items:
            kv=item.info
            values.append(kv['text'])
        return values

    def getFirstValue(self):
        return self.__getValue(0)

    def getLastValue(self):
        return self.__getValue(len(self.__items)-1)

    ##设置选定的值，这里只能是list的文本
    def doSelect(self,targetText):
        targetList=self.__items
        result= self.__selectTargetItem(targetText,targetList)
        return result
        
    
    def __selectTargetItem(self,text,targetList):
        for i in range(len(targetList)):
            kv=targetList[i].info
            value = kv["text"]
            if(text ==value ):
                self.logger.debug("get Target Obj,text=[%s] ,will be Select： info=%s" % (text,kv))
                targetList[i].click()
                return  True
        return False