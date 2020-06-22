import logging
import logging.config
import yaml
import os
import sys
 
print("我要先执行,加载logging配置文件 。。")
def configLoging(path,configFileName):
    configFilePath=os.path.join(path,configFileName)
    print("日志配置文件与路径："+configFilePath)
    with open(configFilePath,'r') as f_conf:
        dict_conf = yaml.safe_load(f_conf)
    logging.config.dictConfig(dict_conf)

configLoging(sys.path[0],'resources/logging.yml')
print("我执行完了,日志配置以及加载")

##静态方法，加载配置文件
def loadConfig(configFileName):
    configFilePath=os.path.join(sys.path[0],configFileName)
    with open(configFilePath,'r') as  f_conf:
        dict_conf = yaml.safe_load(f_conf)
    return dict_conf    