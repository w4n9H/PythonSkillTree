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


from multiprocessing import Process, Queue
import uuid


def process(q):
    """
    test process
    """
    content = str(uuid.uuid4())
    for i in range(4):
        q.put({'content': content})


def main():
    """
    main process
    """
    q = Queue()
    plist = []
    for i in range(4):
        proc = Process(target=process, args=(q,))
        plist.append(proc)
    for proc in plist:
        proc.start()
    for proc in plist:
        proc.join()
    while True:
        if q.empty():
            print "empty"
            break
        else:
            print q.get()

