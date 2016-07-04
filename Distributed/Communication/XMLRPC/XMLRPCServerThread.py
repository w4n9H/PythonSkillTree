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
import SocketServer
import thread


class RPCThreading(SocketServer.ThreadingMixIn, SimpleXMLRPCServer.SimpleXMLRPCServer):
    pass


class MyObject():
    def sayHello(self):
        return "hello xmlprc"


global mutex
mutex = thread.allocate_lock()
server_object = MyObject()
server = RPCThreading(("localhost", 8888))
server.register_instance(server_object)

# Go into the main listener loop
print "Listening"
server.serve_forever()