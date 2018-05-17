#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: main.py

@time: 2018/5/17 下午6:57
"""
import asyncio
from asyncio import ensure_future

from pyppeteer import launch
from pyppeteer.browser import Browser

from core.utils import stringify_dict


async def create_browser():
    _browser = await launch()
    return _browser

browser = None  # type: Browser


def init_chromium():
    global browser
    browser = create_browser()
