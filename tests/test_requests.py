#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: test_requests.py

@time: 2018/5/18 上午1:37
"""

import requests
import time

# start = time.time()
# for i in range(100):
#     r = requests.get("https://www.baidu.com/")
#     # print(r.text)
# print(time.time()-start)
import multiprocessing
print(multiprocessing.cpu_count())