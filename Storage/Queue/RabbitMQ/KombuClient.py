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


from kombu import Connection
from kombu.pools import producers
from kombu.mixins import ConsumerMixin
from kombu import Exchange, Queue


# noinspection PyDefaultArgument,PyAbstractClass,PyPep8Naming
class KomBuClient(ConsumerMixin):
    def __init__(self, hosts_conf, exchange_name='', exchange_type='', exchange_arguments=None,
                 queue_name='', routing_key='', queue_arguments=None, callback=None, no_ack=True):
        self.hosts_conf = hosts_conf
        self.hosts = self.create_hosts()
        self.connection = Connection(self.hosts)
        self.task_exchange = Exchange(name=exchange_name, type=exchange_type, arguments=exchange_arguments)
        self.task_queues = [Queue(name=queue_name, exchange=self.task_exchange, routing_key=routing_key,
                                  queue_arguments=queue_arguments)]
        self.callback = callback
        self.no_ack = no_ack

    def queue_size(self, queue_list, queue_arguments=None):
        result = dict()
        for i in queue_list:
            queue_size = self.connection.SimpleQueue(name=Queue(name=i, queue_arguments=queue_arguments)).qsize()
            result[i] = queue_size
        return result

    def create_hosts(self):
        hosts_list = []
        for i in self.hosts_conf:
            host = i.get('host', '127.0.0.1')
            port = i.get('port', '5672')
            username = i.get('username', 'guest')
            passwd = i.get('passwd', 'guest')
            auth = "amqp://{username}:{passwd}@{host}:{port}//".format(username=username, passwd=passwd,
                                                                       host=host, port=port)
            hosts_list.append(auth)
        return hosts_list

    def get_consumers(self, Consumer, channel):
        channel.basic_qos(prefetch_size=0, prefetch_count=1, a_global=False)
        return [Consumer(queues=self.task_queues,
                         accept=['json', 'pickle', 'msgpack', 'yaml'],
                         callbacks=[self.callback], no_ack=self.no_ack)]

    def process_task(self, body, message):
        print self.hosts
        print body, message.properties
        message.ack()

    def start(self):
        self.run()

    def send_task(self, payload, routing_key=None, priority=0, content_type=None, content_encoding=None,
                  serializer=None, headers=None, compression=None, exchange=None, retry=False,
                  retry_policy=None, declare=[], expiration=None):
        try:
            with producers[self.connection].acquire(block=True) as producer:
                producer.publish(payload,
                                 serializer=serializer, compression=compression, exchange=exchange,
                                 declare=declare, routing_key=routing_key, priority=priority,
                                 content_type=content_type, content_encoding=content_encoding, headers=headers,
                                 retry=retry, retry_policy=retry_policy, expiration=expiration)
        except Exception as error:
            return False, error
        return True, None

    def close(self):
        self.connection.close()