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


import redis


class RedisClient(object):
    def __init__(self, hosts, port, db):
        self.redis_client = redis.Redis(host=hosts, port=port, db=db)

    def get_data(self, key):
        try:
            res_value = self.redis_client.mget(key)
        except Exception, e:
            return str(e)
        return res_value

    def set_string(self, key, value_string):
        self.redis_client.set(key, value_string)

    def set_list(self, key, value_list):
        for i in value_list:
            self.redis_client.rpush(key, i.strip())

    def get_list(self, key):
        return self.redis_client.lrange(key, 0, -1)

    def set_hash(self, key, value_dict):
        return self.redis_client.hmset(key, value_dict)

    def get_hash(self, key):
        return self.redis_client.hgetall(key)

    def set_set(self, key, value_set):
        self.redis_client.sadd(key, value_set)

    def get_set(self, key):
        self.redis_client.spop(key)

    def delete_data(self, key):
        return self.redis_client.delete(key)

    def db_size(self):
        return self.redis_client.dbsize()

    def get_keys(self):
        return self.redis_client.keys()

    def get_type(self, key):
        return self.redis_client.type(key)

    def random_key(self):
        try:
            random_key = self.redis_client.randomkey()
        except Exception, e:
            return str(e)
        return random_key