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


from kazoo.client import KazooClient
import logging
logging.basicConfig()


class ZookeeperClient(object):
    def __init__(self, zk_host):
        self.zk_hosts = zk_host
        self.zk = KazooClient(hosts=self.zk_hosts)

    def connect(self):
        try:
            self.zk.start()
            return 0
        except Exception, e:
            return 1

    def create_node(self, nodename, content):
        try:
            self.zk.create(nodename, content)
            return 0
        except Exception, e:
            print e
            return 1

    def create_ephemeral_node(self, nodename, content):
        try:
            self.zk.create(nodename, content, ephemeral=True)
            return 0
        except Exception, e:
            print e
            return 1

    def create_node_file(self, nodename, configfile_path):
        try:
            with open(configfile_path, 'r') as fp:
                config = fp.read()
            self.zk.create(nodename, config)
            return 0
        except Exception, e:
            print e
            return 1

    def get_data(self, nodename):
        data, stat = self.zk.get(nodename)
        return data, stat

    def set_data(self, namenode, content):
        try:
            self.zk.set(namenode, content)
            return 0
        except Exception, e:
            return 1

    def set_data_file(self, nodename, configfile_path):
        try:
            with open(configfile_path, 'r') as fp:
                config = fp.read()
            self.zk.set(nodename, config)
            return 0
        except Exception, e:
            print e
            return 1

    def delete_node(self, nodename):
        try:
            self.zk.delete(nodename)
            return 0
        except Exception, e:
            print e
            return 1

    def exists_node(self, nodename):
        try:
            result = self.zk.exists(nodename)
            return result
        except Exception, e:
            return 1

    def zk_stop(self):
        self.zk.stop()