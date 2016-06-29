# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/6/29
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


import logging
import tornado.web
import tornado.gen
from tornado.web import HTTPError

import jwt_auth


# noinspection PyAbstractClass
class JWTAuthHandlerV1(tornado.web.RequestHandler):
    def initialize(self):
        pass

    @jwt_auth.jwt_auth
    def get(self, *args, **kwargs):
        try:
            result = args[0]
            if isinstance(result, dict):
                if result['accesskey'] == "abc":
                    self.write("success")
                else:
                    self.write('failed')
            elif isinstance(result, str):
                self.write(result)
            else:
                self.write('error')
        except Exception as error:
            self.write(error)

