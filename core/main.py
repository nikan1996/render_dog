#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: main.py

@time: 2018/5/17 下午6:57
"""
import asyncio
from asyncio import ensure_future, PriorityQueue, Queue
import queue
from pyppeteer import launch
from pyppeteer.page import Page
from pyppeteer.browser import Browser
from pyppeteer.network_manager import Response, NetworkManager
import time

from core.browser_interactive_fuction import disable_image
from core.utils import stringify_dict
import logging
logger = logging.getLogger(__name__)
async def create_browser():
    _browser = await launch()
    return _browser

class Task:
    def __init__(self, *, method=None, url=None, headers=None, cookies=None, data=None, params=None,
        auth=None, json=None, javascript=None):
        self.setup_time = time.time()
        
        # request arguments
        self.method = method
        self.url = url
        self.headers = headers
        self.cookies = cookies
        self.data  = data
        self.params=params
        self.auth = auth
        self.json = json
        self.javascript = None
        self.timeout = None
        
        
        # response arguments
        self.content = None
        self.status_code = None
        self.rsp_headers = None
        self.rsp_cookies = None

        self.done_time = None
        
    def task_done(self):
        self.done_time = time.time()
    
    
    def dump(self):
        return \
            {'task':
                {
                    'task_url': self.url,
                    'request_time': self.setup_time,
                    'done_time': self.done_time,
                    'status_code': self.status_code,
                    'content':self.content,
                }
            }

class ChromiumManager:
    def __init__(self):
        self.task_queue = PriorityQueue()
        self.task_done_queue = Queue
        self.default_browser = None
        self.browsers = {'default_browser': self.default_browser}
        self.pages = {}
    # async def setup_chromium_loop(self):
    #     global browser
    #     browser = await create_browser()
    #     while True:
    #         task = self.task_queue.get()
    #         logger.info()
    #         future = ensure_future()
    async def setup(self):
        self.default_browser = await create_browser()
        print(self.default_browser.wsEndpoint)
        print("chromium version: ", await self.default_browser.version())
        # default page number: 20
        #
        # for i in range(20):
        #     page = await self.default_browser.newPage()
        
    async def get_page_content(self, url, browser=None):
        browser = self.default_browser if not browser else browser
        page = await browser.newPage()  # type: Page
        page.setDefaultNavigationTimeout(30000*10)
        
        # set useragent
        # await page.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.181 Safari/537.36')
        
        # want to disable image loading in page
        #
        # await page.setRequestInterception(True)  # 打开拦截请求开关
        # page.on(NetworkManager.Events.Request, lambda request: disable_image(request))
        response = await page.goto(url)  # type: Response
        content = await page.content()
        title = await page.title()
        
        headers = getattr(response, 'headers', '')
        status_code = getattr(response, 'status', '')
        # await page.close()
        return {
            'content': content,
            'title': title,
            'status_code': status_code,
            'headers': headers
        }
    
    
chromium_manager = ChromiumManager()



