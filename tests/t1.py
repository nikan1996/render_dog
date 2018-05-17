#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: t1.py

@time: 2018/5/17 下午8:17
"""

import requests

r = requests.get("http://0.0.0.0:9999/raw_get_render")
print(r.text)

r2 = requests.get("http://0.0.0.0:9999/raw_get_render")
print(r.text)