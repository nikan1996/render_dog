#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: browser_interactive_fuction.py

@time: 2018/5/19 下午7:37
"""
from asyncio import ensure_future


def disable_image(request):
    """
    disable page from loading images
    """
    if request._resourceType == 'image':
        ensure_future(request.abort())
    else:
        ensure_future(request.continue_())