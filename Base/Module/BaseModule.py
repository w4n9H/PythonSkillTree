# !/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@author: mango
@contact: w4n9@sina.com
@create: 16/7/8
hail hydra!
"""

__author__ = "mango"
__version__ = "0.1"


def bisect_demo():
    """
    为可排序列表提供二分查找算法
    :return:
    """
    import bisect
    demo_list = [2, 6, 1, 8, 4, 9, 0]
    demo_list.sort()
    bisect.insort(demo_list, 5)
    print demo_list
    print bisect.bisect(demo_list, 3)


if __name__ == '__main__':
    bisect_demo()
