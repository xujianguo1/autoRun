import logging
import logging.config
import yaml

def configLoging(configFilePath):
    with open(configFilePath,'r') as f_conf:
        dict_conf = yaml.safe_load(f_conf)
    logging.config.dictConfig(dict_conf)




