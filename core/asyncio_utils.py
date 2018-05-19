#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: asyncio_utils.py

@time: 2018/5/18 下午6:06
"""

async def add_future_callback(fut, success_callback, fail_callback=None, need_fut_as_success_cb_args=True):
    """
    adding a callback after future completed
    
    :param fut:
    :param callback:
    :param args:
    :return:
    """
    try:
        result = await fut
        if need_fut_as_success_cb_args:
            await success_callback(result)
        else:
            await success_callback()
    except Exception:
        if fail_callback:
            await fail_callback()
        raise

    return result
