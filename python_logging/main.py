import logging.config

import submod1
logging.config.fileConfig('conf')


root_logger = logging.getLogger('root')

root_logger.debug('this is debug message in main.py')
root_logger.info('this is info message in main.py')
root_logger.warn('this is warn message in main.py')
root_logger.error('this is error message in main.py')


submod1.func1()
