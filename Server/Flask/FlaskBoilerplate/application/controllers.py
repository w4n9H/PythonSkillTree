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

from flask import Flask, request, Response
from flask import render_template, url_for, redirect, send_from_directory
from flask import send_file, make_response, abort

from application import app

# routing for API endpoints, generated from the models designated as API_MODELS
# from application.core import api_manager
# from application.models import *


# routing for basic pages (pass routing onto the Angular app)
@app.route('/', methods=['GET'])
def show_entries():
    return render_template('index.html')