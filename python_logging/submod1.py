import logging

from logging_test.mulmod.submod2 import func2

logger = logging.getLogger()

logger.info('this is info message in submod1.py')


def func1():
    logger.info('this is info message in function func1 in submod1.py')

    func2()
