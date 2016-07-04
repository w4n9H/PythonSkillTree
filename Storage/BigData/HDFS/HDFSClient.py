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


from snakebite.client import Client


class HDFSClient(object):
    def __init__(self, host, port):
        self.hdfs_host = host
        self.hdfs_port = port
        try:
            self.client = Client(self.hdfs_host, int(self.hdfs_port))
        except Exception, e:
            print str(e)

    def list_dir(self, path):
        """
        列出目录的文件
        :param path: 文件夹路径
        :return: 返回一个文件列表
        """
        file_list = []
        try:
            for x in self.client.ls([path]):
                file_path = x.get('path', None)
                file_list.append(file_path)
        except Exception, e:
            return 1, str(e)
        return 0, file_list

    def exists_dir(self, path):
        """
        判断hdfs文件夹是否存在
        :param path: 文件夹路径
        :return: True 文件夹存在   False 文件夹不存在
        """
        return self.client.test(path, exists=True, directory=True)

    def exists_file(self, path):
        """
        判断文件是否存在
        :param path: 文件路径
        :return: True 文件存在   False 文件不存在
        """
        return self.client.test(path, exists=True, directory=False)

    def get_zero_list(self, path, start_time=None, stop_time=None):
        """
        列出目录内文件的大小
        :param path: 文件夹路径
        :return:
        """
        file_list = []
        if start_time and stop_time:
            pass
        try:
            for x in self.client.ls([path]):
                if x['file_type'] == 'f':
                    if x['length'] == 0:
                        file_list.append(x['path'])
        except Exception, e:
            return 1, str(e)
        return 0, file_list

    def delete_paths(self, path):
        """
        删除文件
        :param path: 文件夹路径 list
        :return:
        """
        try:
            self.client.delete(path)
        except Exception, e:
            return 1, str(e)
        return 0, None

    def delete_dir(self, dir_path):
        """

        :param dir_path:
        :return:
        """
        try:
            self.client.rmdir(dir_path)
        except Exception, e:
            return 1, str(e)
        return 0, None