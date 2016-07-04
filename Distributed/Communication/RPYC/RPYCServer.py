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


import rpyc


# noinspection PyMethodMayBeStatic
class RPYCTestServer(rpyc.Service):
    def on_connect(self):
        pass

    def on_disconnect(self):
        pass

    def exposed_get_answer(self):
        return 42

    def exposed_question(self):
        return "RPYC!"


if __name__ == "__main__":
    from rpyc.utils.server import ThreadedServer
    t = ThreadedServer(RPYCTestServer, port=18861)
    t.start()
