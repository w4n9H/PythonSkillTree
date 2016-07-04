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


import os, sys
import happybase
import uuid


class HBaseClient(object):
    def __init__(self, hbase_host):
        """
        初始化,连接hbase
        :param hbasehost: 连接主机 (str)
        :return: None
        """
        try:
            self.connection = happybase.Connection(hbase_host)
        except Exception, e:
            print e

    def create_table(self, table_name, families):
        """
        新建表
        :param table_name: 表名 (str)
        :param families: 列族的选项 (dict)
          {'列族': dict()}  使用默认配置
          {'列族': dict(max_versions=1, TTL=3600)}  使用自定义配置
        :return:
          成功返回 0  None
          失败返回 1  错误信息
        """
        try:
            self.connection.create_table(table_name, families)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def table_disable(self, table_name):
        """
        禁用表
        :param table_name : 表名 (str)
        :return :
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.connection.disable_table(table_name)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def table_enable(self, table_name):
        """
        启用表
        :param table_name : 表名 (str)
        :return :
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.connection.enable_table(table_name)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def table_status(self, table_name):
        """
        检查表状态,是否启用
        """
        pass

    def delete_table(self, table_name):
        """
        删除指定表   *****注意:这个函数慎用,不用禁用表即可删除表,不要误删除*****
        :param table_name: 表名 (str)
        :return:
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.connection.delete_table(table_name, disable=True)
        except Exception, e:
            return 1 , str(e)
        return 0, None

    def conn_table(self, table_name):
        """
        连接表
        :param: table_name: 表名 (str)
        :return:
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.table = self.connection.table(table_name)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def put_data(self, row_name, data_dict):
        """
        写入数据
        :param row_name: 行 (str)
        :param data_dict: 写入的数据 (dict)
          {'column_name:column_num':'data_value'} eg:{'t1:1':'value'}
        :return:
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.table.put(row_name, data_dict)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def show_one_data(self, row_key, column):
        """
        显示单条数据
        :param row_key: 行key (str)
        :param column: 指定的列 列族+列修饰符 'f1:1' (str)
        :return:
          成功返回 0 数据信息
          失败返回 1 错误信息
        """
        try:
            row = self.table.row(row_key)
        except Exception, e:
            return 1, str(e)
        return 0, row[column]

    def show_data(self, row_key_list):
        """
        查询一个或多个row_key的全部内容
        :param row_key_list: row_key列表 ['r1','r2',.....] (list)
        :return:
          返回一个列表,每个行key为一个元祖,包含一个key和字典
          [('test_data', {'result:test': '123456123'})])
        """
        try:
            return 0, self.table.rows(row_key_list)
        except Exception, e:
            return 1,str(e)

    def delete_row(self, row_key):
        """
        删除表中指定行的所有内容
        :param row_key: 行key (str)
        :return:
          成功返回 0 None
          失败返回 1 错误信息
        """
        try:
            self.table.delete(row_key)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def delete_column(self, row_key, column):
        """
        删除表中指定列族或者指定列的数据
        :param row_key: key
        :param column: 列族或指定列 ['f1'] or ['f1:1'] (list)
        :return:
        """
        try:
            self.table.delete(row_key, columns=column)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def close_conn(self):
        """
        关闭连接
        :return:
        """
        self.connection.close()