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


import SimpleXMLRPCServer


class MyObject():
    def sayHello(self):
        return "hello xmlprc"


obj = MyObject()
server = SimpleXMLRPCServer.SimpleXMLRPCServer(("localhost", 80))
server.register_instance(obj)


print "Listening on port 80"
server.serve_forever()