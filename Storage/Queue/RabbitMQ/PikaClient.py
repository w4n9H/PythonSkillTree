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


import pika
import pika.credentials


# noinspection PyBroadException
class PIKAClient(object):
    def __init__(self, host, port=5672, username='guest', password='guest', prefetch_count=1):
        """
        初始化rmq类
        :param host:
        :param port:
        :param username:
        :param password:
        :param prefetch_count:
        :return:
        """
        self.queue_host = host
        self.queue_port = port
        self.credentials = pika.credentials.PlainCredentials(username=username, password=password)
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host=self.queue_host,
                                                                            port=self.queue_port,
                                                                            credentials=self.credentials))
        self.channel = self.connection.channel()
        self.channel.basic_qos(prefetch_count=prefetch_count)

    def create_queue(self, queue_name, durable=True, auto_delete=False, args=None):
        """
        声明队列
        :param queue_name: 队列名称 str
        :param durable: 是否持久化 bool
        :param auto_delete: 是否自动删除 bool
        :param args:
        :return:
        """
        if not args:
            args = {}
        try:
            self.channel.queue_declare(queue=queue_name, durable=durable, auto_delete=auto_delete, arguments=args)
        except:
            return False
        return True

    def create_exchange(self, exchange_name, ex_type='direct', durable=False):
        """
        声明 exchange
        :param exchange_name: exchange 名称 str
        :param ex_type: 分发类型 str
        :param durable: 是否持久化  bool
        :return:
        """
        try:
            self.channel.exchange_declare(exchange=exchange_name, type=ex_type, durable=durable)
        except:
            return False
        return True

    def bind_queue(self, exchange_name, queue_name, routing_key='', ex_type='fanout', durable=True, auto_delete=False, args=None):
        """
        绑定 exchange 和 queue
        :param exchange_name: exchange 名 str
        :param queue_name: 队列名 str
        :param routing_key: key  str
        :param ex_type: 'direct', 'topic', and 'fanout' 分发类型 str
        :param durable: 是否持久化 bool
        :param auto_delete: 是否自动删除 bool
        :param args: 其他参数 dict
        :return:
        """
        if not args:
            args = {}
        try:
            self.create_queue(queue_name, durable=durable, auto_delete=auto_delete, args=args)
            self.create_exchange(exchange_name, ex_type=ex_type, durable=durable)
            # self.channel.queue_declare(queue=queue_name, durable=durable, auto_delete=auto_delete, arguments=args)
            self.channel.queue_bind(exchange=exchange_name, queue=queue_name, routing_key=routing_key)
            return True
        except:
            return False

    def delete_queue(self, queue_name):
        """
        删除队列
        :param queue_name: 队列名 str
        :return:
        """
        try:
            self.channel.queue_delete(queue=queue_name)
            return True
        except:
            return False

    def delete_exchange(self, exchange_name):
        """
        删除exchange
        :param exchange_name: exchange 名 str
        :return:
        """
        try:
            self.channel.exchange_delete(exchange=exchange_name)
            return True
        except:
            return False

    def write_exchange(self, exchange_name, content, routing_key=''):
        """
        写消息到exchange
        :param exchange_name: exchange 名称 str
        :param content: 内容 str
        :param routing_key: key str
        :return:
        """
        try:
            self.channel.basic_publish(exchange=exchange_name, routing_key=routing_key, body=content)
            return True
        except Exception, err:
            print err
            return False

    def write_queue(self, queue_name, content):
        """
        只写队列
        :param queue_name: 队列名称 str
        :param content:
        :return:
        """
        try:
            self.channel.basic_publish(exchange='', routing_key=queue_name, body=content)
            return True
        except Exception, err:
            print err
            return False

    def read_queue(self, queue_name):
        """
        获取队列内容
        :param queue_name: 队列名 str
        :return:
        """
        method_frame, header_frame, body = self.channel.basic_get(queue=queue_name, no_ack=True)
        return method_frame, body

    def start_consuming(self, queue_name, processor, no_ack=False):
        """
        持续获取队列内容
        :param queue_name: 队列名称 str
        :param processor: 回调函数  func
        :param no_ack: 是否ack bool
        :return:
        """
        self.channel.basic_consume(processor, queue=queue_name, no_ack=no_ack)
        self.channel.start_consuming()

    def close(self):
        """
        关闭连接
        :return:
        """
        self.connection.close()