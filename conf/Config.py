import logging
import logging.config
import yaml
import os
import sys
 
print("我要先执行,配置文件路径，运行目录/resources/logging.yml")
def configLoging(configFilePath):
    with open(configFilePath,'r') as f_conf:
        dict_conf = yaml.safe_load(f_conf)
    logging.config.dictConfig(dict_conf)

configLoging(os.path.join(sys.path[0],'resources/logging.yml'))
print("我执行完了,日志配置以及加载")