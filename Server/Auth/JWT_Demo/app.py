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


import os
import logging
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web
from tornado.options import options, define
from tornado.web import url


from handlers import handler


# noinspection PyAbstractClass
class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r'/v1/jwt_auth', handler.JWTAuthHandlerV1),
        ]
        settings = {
            'static_path': os.path.join(os.path.dirname(__file__), 'static'),
            'template_path': os.path.join(os.path.dirname(__file__), 'templates'),
            'xsrf_cookies': False,
            'debug': False,
            'autoescape': None,
        }
        tornado.web.Application.__init__(self, handlers, **settings)


def main():
    # --log-rotate-mode=time --log_file_num_backups=1
    define("port", default=8080, type=int)
    define("log_file_prefix", default="tornado.log")
    define("log_to_stderr", default=True)
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application(), max_buffer_size=1024 * 1024 * 1024)
    http_server.listen(options.port)
    logging.info("start tornado server on port: %s" % options.port)
    tornado.ioloop.IOLoop.instance().start()


if __name__ == '__main__':
    main()

