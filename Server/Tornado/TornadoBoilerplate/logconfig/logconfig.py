# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/6/30
hail hydra!
An extended version of the log_settings module from zamboni:
https://github.com/jbalogh/zamboni/blob/master/log_settings.py
"""
from __future__ import absolute_import

from tornado.log import LogFormatter as TornadoLogFormatter
import logging
import logging.handlers
import logging.config
import os.path
import types


def initialize_logging():
    cfg = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
                'datefmt': "%Y-%m-%d %H:%M:%S"
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'logging.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'verbose',
                'stream': 'ext://sys.stdout'
            },
            'file': {
                'level': 'DEBUG',
                'class': 'logging.handlers.RotatingFileHandler',
                # 当达到10MB时分割日志
                'maxBytes': 1024 * 1024 * 10,
                # 最多保留50份文件
                'backupCount': 50,
                # If delay is true,
                # then file opening is deferred until the first call to emit().
                'delay': True,
                'filename': 'mysite.log',
                'formatter': 'verbose'
            }
        },
        'loggers': {
            '': {
                'handlers': ['file', 'console'],
                'level': 'INFO',
            },
        }
    }
    logging.config.dictConfig(cfg)
