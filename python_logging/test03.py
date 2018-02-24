# encoding: utf-8
import logging.config
logging.config.fileConfig('logging.config')

import test0301
mylogger = logging.getLogger('mine')       # 配置文件里没配置的名字会默认为root, 所以必须配置root
yourlogger = logging.getLogger('main')
mainlogger = logging.getLogger('test03')       # 这里的名字是qualname

mylogger.error('my log')
yourlogger.error('your log')
mainlogger.error('this is test03 module')

test0301.test0301()