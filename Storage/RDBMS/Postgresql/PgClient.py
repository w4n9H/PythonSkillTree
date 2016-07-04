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


import psycopg2


class PGClient(object):
    """
    Postgresql 管理类
    """
    def __init__(self, host='localhost', port=5432, user='user', password='passwd', database='database'):
        """
        初始化函数
        """
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.database = database
        self.conn_string = "host=%s port=%s user=%s password=%s dbname=%s" % \
                           (self.host, self.port, self.user, self.password, self.database)
        self.conn = psycopg2.connect(self.conn_string)

    def create_cursor(self):
        """
        创建 cursor
        """
        self.cursor = self.conn.cursor()

    def close_cursor(self):
        """
        关闭  cursor
        """
        self.cursor.close()

    def pg_commit(self):
        """
        提交 commit
        """
        try:
            self.conn.commit()
            return 1
        except psycopg2.Error, err:
            #print err
            return 0

    def close_conn(self):
        """
        关闭 conn
        """
        self.conn.close()

    def close_save(self):
        """
        把commit和close合并起来
        """
        self.conn.commit()
        self.cursor.close()
        #self.conn.close()

    def pg_query(self, query_sql):
        """
        sql 查询函数

        :param str query_sql: 数据库查询语句
        :return : 以list的形式返回查询数据
        :rtype : list
        """
        #self.create_cursor()
        try:
            self.cursor.execute(query_sql)
            return_data = self.cursor.fetchall()
            #self.close_cursor()
            #self.close_conn()
            return return_data
        except psycopg2.Error, err:
            print err

    def pg_insert(self, data_table, data_dict):
        """
        sql 插入数据

        :param data_table:需要插入数据的表
        :param data_dict:要插入的数据(dict)
        :return 1: TRUE 插入成功
        :return 0: FALSE 插入数百
        """
        key_string = ''
        value_string = ''
        for dict_key, dict_value in data_dict.iteritems():
            key_string += '%s,' % dict_key
            value_string += "%%(%s)s" % dict_key + ','
        #
        insert_sql = """INSERT INTO %s (%s) VALUES (%s);""" % (data_table, key_string[:-1], value_string[:-1])
        try:
            self.cursor.execute(insert_sql, data_dict)
            return 1
        except psycopg2.Error, err:
            self.conn.rollback()
            print err
            return 0

    def pg_update(self, tablename, up_data_dict, condition_string):
        """
        "update apt_source set (aptname,md5) = (%(aptname)s,%(md5)s) where id=1;"

        :param update_sql:sql语句 "update apt_source set %s where id=4586"
        :param up_data_dict:需要插入的数据,type:dict
        :return: 成功返回1,失败返回0
        """
        update_string = ''
        for dict_key, dict_value in up_data_dict.iteritems():
            update_string += '%s=%%(%s)s,' % (dict_key, dict_key)
        update_sql = """UPDATE %s SET %s WHERE %s;""" % (tablename, update_string.rstrip(','), condition_string)
        try:
            self.cursor.execute(update_sql, up_data_dict)
            return 1
        except psycopg2.Error, err:
            self.conn.rollback()
            print err
            return 0

    def pg_update_bulk(self, tablename, up_data_list, begin_id):
        """
        一次更新多条数据
        :param tablename:需要update的表
        :param up_data_list:需要插入的数据,type:list list内嵌dict
        :param begin_id:需要修改的数据的起始id
        """
        dict_num = 0
        id = begin_id
        while id < begin_id+len(up_data_list):
            up_data_dict = up_data_list[dict_num]
            update_string = ''
            for dict_key, dict_value in up_data_dict.iteritems():
                update_string += '%s=%%(%s)s,' % (dict_key, dict_key)
            update_sql = """UPDATE %s SET %s WHERE id=%s;""" % (tablename, update_string.rstrip(','), str(id))
            self.cursor.execute(update_sql, up_data_dict)
            id += 1
            dict_num += 1

    def pg_del(self, table_name, del_id):
        """
        删除某一行数据
        :param table_name:要删除的目标table
        :param del_id:要删除的id
        :return:成功返回1,失败返回0
        """
        del_sql = """DELETE FROM %s WHERE ID=%s;""" % (table_name, del_id)
        try:
            self.cursor.execute(del_sql)
            return 1
        except psycopg2.Error, err:
            print err
            return 0

