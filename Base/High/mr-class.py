# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/9/7
hail hydra!
"""


__author__ = "mango"
__version__ = "0.1"


import os
from threading import Thread


class GenericInputData(object):
    def read(self):
        raise NotImplementedError    # read 方法必须由子类实现

    @classmethod    # classmethod 的用法
    def generate_inputs(cls, config):
        raise NotImplementedError


class PathInputData(GenericInputData):
    def __init__(self, path):
        super(PathInputData, self).__init__()    # 使用super初始化父类
        self.path = path

    def read(self):
        return open(self.path).read()

    @classmethod
    def generate_inputs(cls, config):
        data_dir = config['data_dir']
        for name in os.listdir(data_dir):
            yield cls(os.path.join(data_dir, name))    # yield 的用法


class GenericWorker(object):
    def __init__(self, input_data):
        self.input_data = input_data
        self.result = None

    def map(self):
        raise NotImplementedError

    def reduce(self, other):
        raise NotImplementedError

    @classmethod
    def create_workers(cls, input_class, config):
        workers = []
        for input_data in input_class.generate_inputs(config):
            workers.append(cls(input_data))
        return workers


class LineCountWorker(GenericWorker):
    def map(self):
        data = self.input_data.read()
        self.result = len(data.split(' '))

    def reduce(self, other):
        self.result += self.result


# 只在使用Mix-in组件制作工具类时进行多重继承
class ToDictMixin(object):
    def to_dict(self):    # public 属性
        return self._traverse_dict(self.__dict__)

    def _traverse_dict(self, instance_dict):    # private 属性
        output = {}
        for k, v in instance_dict.items():
            output[k] = self._traverse(k, v)
        return output

    def _traverse(self, k, v):
        if isinstance(v, ToDictMixin):    # 动态判断对象类型
            return v.to_dict()
        elif isinstance(v, dict):
            return self._traverse_dict(v)
        elif isinstance(v, list):
            return [self._traverse(k, i) for i in v]
        elif hasattr(v, '__dict__'):    # 动态访问属性
            return self._traverse_dict(v.__dict__)
        else:
            return v


class WorkDir(ToDictMixin):
    def __init__(self, v):
        self.data_dir = v


def execute(workers):
    threads = [Thread(target=w.map) for w in workers]
    for thread in threads: thread.start()
    for thread in threads: thread.join()
    first, rest = workers[0], workers[1:]
    for worker in rest:
        first.reduce(worker)
    return first.result


def map_reduce(worker_class, input_class, config):
    workers = worker_class.create_workers(input_class, config)
    return execute(workers)


work_dir = WorkDir('data')
config = work_dir.to_dict()
print map_reduce(LineCountWorker, PathInputData, config)
