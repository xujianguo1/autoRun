import os
import sys
from app import Config
import logging


runPath= sys.path[0]
print("run path=%s" % runPath)
#配置log
Config.configLoging(os.path.join(runPath,'resources/logging.yml'))




def logtest1():
    logger = logging.getLogger('simpleExample')
    logger.debug('debug message')
    logger.info('info message')
    logger.warning('warn message')
    logger.error('error message')
    logger.critical('critical message')    


def logtest2():
    logger = logging.getLogger(__name__)
    logger.debug('debug message222222')
    logger.info('info message22222')
    logger.warning('warn message2222222')
    logger.error('error message2222222')
    logger.critical('critical message222222')  
def logtest3():
    logger = logging.getLogger('fileExample')
    logger.debug('debug message fileExample')
    logger.info('info message fileExample')
    logger.warning('warn message fileExample')
    logger.error('error message fileExample')
    logger.critical('critical message fileExample')  


if (__name__=="__main__"):
   
    logtest1()
    logtest2()
    logtest3()

