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


import etcd


# noinspection PyBroadException,PyPep8Naming,PyShadowingBuiltins
class ETCDClient(object):
    def __init__(self, host, port, allow_reconnect=True, protocol='http'):
        self.client = etcd.Client(host=host, port=port, allow_reconnect=allow_reconnect, protocol=protocol)

    def set_key(self, key, value, ttl=None, append=False, prevExist=False):
        """
        设置kv对
        :param key: 键 (str)
        :param value: 值 (str)
        :param ttl: 生存时间/秒 (int)
        :param append: 目录中添加值,key默认数字,由低到高 (bool)
        :param prevExist:
        True 如果存在先前节点,插入成功，不存在插入失败
        False 如果存在先前节点,插入失败,不存在插入成功  (bool)
        :return:
        """
        try:
            self.client.write(key, value, ttl=ttl, append=append, prevExist=prevExist)
        except Exception as error:
            return False, error
        return True, None

    def set_dir(self, dir_name):
        """
        创建目录
        :param dir_name: 目录 (str)
        :return:
        """
        try:
            self.client.write(dir_name, dir=True)
        except:
            return False
        return True

    def get_key(self, key, wait=False, recursive=False, sorted=False):
        r = None
        try:
            r = self.client.read(key, wait=wait, recursive=recursive, sorted=sorted)
        except:
            pass
        finally:
            return r

    def delete_key(self, key, dir=False, recursive=False):
        try:
            self.client.delete(key, dir=dir, recursive=recursive)
        except Exception as error:
            return False, error
        return True, None

    def update_key(self, key, new_value):
        """
        更新key,实际这个参数更暴力,建议使用 write
        :param key:
        :param new_value:
        :return:
        """
        try:
            result = self.client.read(key)
            result.value = new_value
            self.client.update(result)
        except Exception as error:
            return False, error
        return True, None

    def get_value(self, etcd_path):
        r = self.get_key(etcd_path)
        if r:
            return json.loads(r.value)
        else:
            return None


if __name__ == '__main__':
    p = ETCDClient(host='xxx.xxx.xxx.xxx', port=2379, allow_reconnect=True)
    import json
    print p.set_key('/test/node1', json.dumps({'a': 'b'}), ttl=3)
    print p.get_key('/test/node1')