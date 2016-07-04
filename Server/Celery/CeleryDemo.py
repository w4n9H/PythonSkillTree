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


from celery import Celery
import time


celery_config = {
    'celery_name': 'tasks',
    'celery_backend': 'amqp',
    'celery_accept_content': ['pickle', 'json', 'msgpack', 'yaml'],
    'broker_url': 'amqp://guest:guest@192.168.13.193:5672//',
    'celery_task_serializer': 'json',
    'celery_result_serializer': 'json'
}


celery = Celery(celery_config['celery_name'], backend=celery_config['celery_backend'])

celery.conf.update(
    CELERY_TASK_SERIALIZER=celery_config['celery_task_serializer'],
    CELERY_ACCEPT_CONTENT=celery_config['celery_accept_content'],
    CELERY_RESULT_SERIALIZER=celery_config['celery_result_serializer'],
    BROKER_URL=celery_config['broker_url']
)


@celery.task()
def add(x):
    time.sleep(1)
    return x