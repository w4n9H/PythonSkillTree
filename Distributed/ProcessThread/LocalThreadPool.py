# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/7/4
hail hydra!
pip install threadpool
源码中有提供一个示例
"""

__author__ = "mango"
__version__ = "0.1"


import threadpool
import time
import traceback


def callback_func():
    pass


def exc_callback(excinfo):
    errorstr = ''.join(traceback.format_exception(*excinfo))
    print errorstr


def now_time(n):
    print 'Starting at %s' % time.ctime()
    time.sleep(n)
    return 'Ending at %s' % time.ctime()


def print_now(request, n):
    print '%s - %s' % (request.requestID, n)  # 这里的requestID只是显示下，没实际意义

pool = threadpool.ThreadPool(5)
reqs = threadpool.makeRequests(now_time, range(1, 11), print_now)
[pool.putRequest(req) for req in reqs]
pool.wait()