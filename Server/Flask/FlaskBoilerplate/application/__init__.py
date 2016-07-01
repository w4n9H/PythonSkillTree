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


import os
import json
from flask import Flask, request, Response
from flask import render_template, send_from_directory, url_for

app = Flask(__name__)

app.config.from_object('application.settings')

app.url_map.strict_slashes = False

# import application.core
# import application.models
import application.controllers