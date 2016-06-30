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


import tornado
import tornado.template
from tornado.options import define, options

import os
from logconfig import logconfig

# Make file paths relative to settings.
get_path = lambda root, *a: os.path.join(root, *a)
ROOT = os.path.dirname(os.path.abspath(__file__))

define("port", default=8888, help="run on the given port", type=int)
define("config", default=None, help="tornado config file")
define("debug", default=False, help="debug mode")
tornado.options.parse_command_line()

MEDIA_ROOT = get_path(ROOT, 'media')
TEMPLATE_ROOT = get_path(ROOT, 'templates')


# Deployment Configuration 部署配置
# settings 配置
settings = dict()
settings['debug'] = True
settings['static_path'] = MEDIA_ROOT
settings['cookie_secret'] = "your-cookie-secret"
settings['xsrf_cookies'] = True
settings['template_loader'] = tornado.template.Loader(TEMPLATE_ROOT)


# log 配置
logconfig.initialize_logging()

if options.config:
    tornado.options.parse_config_file(options.config)
