#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: test_chromium_performance.py

@time: 2018/5/18 上午1:09
"""
import asyncio
from asyncio import ensure_future
from pyppeteer import launch
from core.main import init_chromium_loop
import time
import uvloop
import random
asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())

async def get_baidu_page(browser):
    page = await browser.newPage()
    start = time.time()

    result = await page.goto("https://www.baidu.com/")
    content = await page.content()
    stop = time.time()
    print(stop - start)
    # print(content)
    return content
    # print(1)

async def init_browser():
    browser = await launch()
    return browser
    
async def test_chromium_performance():
    for i in range(10):
        print(i)
        browser1 = await launch()
        start = time.process_time()
        page = await browser1.newPage()
        start = time.time()
    
        result = await page.goto("https://www.baidu.com/")
        content = await page.content()
        stop = time.time()
        print(stop - start)
        # print(content)
    
        # print(stop - start)
        await browser1.close()
    
if __name__ == '__main__':
    # print(1)
    # test_chromium_performance()
    asyncio.get_event_loop().run_until_complete(test_chromium_performance())
    