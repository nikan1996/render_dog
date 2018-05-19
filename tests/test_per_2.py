#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: test_chromium_performance.py

@time: 2018/5/18 上午1:09
"""
import asyncio
import random
from asyncio import ensure_future
from functools import partial
from pyppeteer import launch
import time
import uvloop
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def add_success_callback(fut, callback):
    print(callback)
    result = await fut
    await callback(result)
    return result

async def get_baidu_page(browser, page=None):
    print(browser)
    print(1)
    start = time.time()
    page = await browser.newPage() if page is None else page
    stop = time.time()

    print("new page cost", stop - start)
    print(3)
    
    version = await browser.version()
    print("new version cost", time.time() - stop)
    start = time.time()
    # result = await page.goto("https://www.baidu.com/")
    time1 = time.time()
    # print(await result.text())
    time2 = time.time()
    
    content = await page.content()
    print(content)
    time3 = time.time()
    # print(time2 - time1)
    print(time3-time2)
    print('hhhh')
    stop = time.time()
    print(stop - start)

    return content


async def init_browser():
    browser = await launch()
    return browser


async def main():
    print('run main')
    browser1 = await launch()
    browser2 = await launch()
    pages = []
    print(0)
    for i in range(1):
        page = ensure_future(browser1.newPage())
        ensure_future(add_success_callback(page, partial(get_baidu_page, browser1)))
        # page.add_done_callback(partial(get_baidu_page, browser1))
        pages.append(page)
        print(i)
    # asyncio.wait(ensure_future(pages))
    # await get_baidu_page(browser1)
    print('__init__ browser')
    # futures = []
    # for i in range(100):
        # futures.append(ensure_future(get_baidu_page(random.choice([browser1,]), pages[i])))
    # asyncio.gather(futures)
    
    print(2)
    # await browser.close()
    print(2)


if __name__ == '__main__':
    fu = ensure_future(main())
    asyncio.get_event_loop().run_forever()
