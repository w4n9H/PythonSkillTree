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


import xmlrpclib

server = xmlrpclib.ServerProxy("http://localhost:8888")

words = server.sayHello()

print "result:" + words