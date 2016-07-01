# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/7/1
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


from multiprocessing import Manager, Pool


def process(q, name):
    """
    test process
    """
    q.put(1)


def main():
    """
    main process
    """
    m = Manager()
    q = m.Queue()
    plist = []
    pool = Pool(processes=20)
    for proc in plist:
        pool.apply_async(process, (q, proc))
    pool.close()
    pool.join()
    count = 0
    while True:
        if q.empty():
            print "empty"
            break
        else:
            c = q.get()
            print c
            count += c
    print count
if __name__ == '__main__':
    main()

