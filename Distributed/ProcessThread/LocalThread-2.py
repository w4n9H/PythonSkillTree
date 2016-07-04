# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/7/4
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


import threading, time
from time import sleep, ctime


def now():
    return str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()))


class myThread (threading.Thread):
    def __init__(self, nloop, nsec):
        super(myThread, self).__init__()
        self.nloop = nloop
        self.nsec = nsec

    def run(self):
        print 'start loop', self.nloop, 'at:', ctime()
        sleep(self.nsec)
        print 'loop', self.nloop, 'done at:', ctime()


def main():
     thpool = []
     print 'starting at:', now()
     for i in xrange(10):
         thpool.append(myThread(i, 2))
     for th in thpool:
         th.start()
     for th in thpool:
         th.join()
     print 'all Done at:', now()


if __name__ == '__main__':
        main()