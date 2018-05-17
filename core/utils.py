#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: utils.py

@time: 2018/5/17 下午3:48
"""


def stringify_dict(_dict):
    """make all dict values to be string type"""
    new_dict = dict((key, str(value)) for key, value in _dict.items())
    print(new_dict)
    return new_dict