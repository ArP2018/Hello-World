from threading import Thread
from time import ctime


class MyThread(Thread):
    def __init__(self, tar_func, args, name):
        Thread.__init__(self)
        self.tar_func = tar_func
        self.args = args
        self.name = self.name

    def run(self):
        print('starting %s at %s' % (self.name, ctime()))
        self.res = self.tar_func(*self.args)
        print('finished %s at %s' % (self.name, ctime()))

    def get_result(self):
        return self.res
