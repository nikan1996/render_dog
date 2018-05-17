#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: 1.py

@time: 2018/5/17 下午1:26
"""
import asyncio
from asyncio import ensure_future

from pyppeteer import launch

from core.utils import stringify_dict


async def main():
    browser = await launch()
    page = await browser.newPage()
    result = await page.goto("https://www.baidu.com/")
    content = await page.content()
    print(content)
    cookie = await page.cookies()
    print(cookie)
    await page.setCookie(stringify_dict({'name': 'password', 'value': 123456}))
    cookie = await page.cookies()
    print(cookie)
    # print(content)
    result = browser.wsEndpoint
    print(result)
    print(1)
    # version = await browser.version()
    print(2)
    page = await browser.newPage()
    result = await page.goto("https://www.baidu.com/")
    # content = await page.content()
    # print(content)
    # result = page.setCookie({'1': 1})
    coo = await page.cookies()
    print(coo)

    # print(result)
    # assert version is not None
    # print(version)
    # await browser.close()
    return content

if __name__ == '__main__':
    future = ensure_future(main())
    asyncio.get_event_loop().run_forever()