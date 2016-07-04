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


from datetime import datetime
from elasticsearch import Elasticsearch


class AvlESAdm(object):
    def __init__(self, host_list):
        self.es = Elasticsearch(hosts=host_list)

    def creat_index(self, index_name):
        """
        新建索引
        :param index_name: 索引名称 str
        :return:
        """
        try:
            self.es.indices.create(index=index_name)
            return True
        except Exception, e:
            print e
            return False

    def delete_index(self, index_name):
        """
        删除索引
        :param index_name: 索引名称 str
        :return:
        """
        try:
            self.es.indices.delete(index=index_name)
            return True
        except Exception, e:
            print e
            return False


class AvlESClient(object):
    def __init__(self, host_list, index, doc_type):
        """
        初始化
        :param host_list:   host列表 list
        :param index: 索引名称  str
        :param doc_type: doc_type  str
        :return:
        """
        self.index = index
        self.doc_type = doc_type
        try:
            self.es = Elasticsearch(hosts=host_list)
        except Exception, e:
            print e

    def put_index(self, id, data):
        """
        向索引插入数据,修改数据
        :param id: id不能重复  int
        :param data: 数据  dict  {"any": "data", "timestamp": datetime.now()}
        :return: true or false
        """
        try:
            self.es.index(index=self.index, doc_type=self.doc_type, id=id, body=data)
            return True
        except Exception, e:
            print e
            return False

    def get_data(self, id):
        """
        查询数据
        :param id: id号  int
        :return:成功返回数据  失败返回false
        """
        try:
            result = self.es.get(index=self.index, doc_type=self.doc_type, id=id)
            return result
        except Exception, e:
            print e
            return False

    def exists_data(self, id):
        """
        判断数据是否存在
        :param id: id号 int
        :return:存在返回true 不存在返回false
        """
        try:
            if self.es.exists(index=self.index, doc_type=self.doc_type, id=id):
                return True
            else:
                return False
        except Exception, e:
            print e

    def search(self):
        """
        查询数据
        :return:
        """
        res = self.es.search(index=self.index, body={"query": {"match_all": {}}})
        print("Got %d Hits:" % res['hits']['total'])
        for hit in res['hits']['hits']:
            print hit["_source"]