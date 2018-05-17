#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: render.py

@time: 2018/5/17 下午11:39
"""
from aiohttp import web


class RenderView(web.View):
    async def get(self):
        return await raw_get_render(self.request)

    async def post(self):
        return await raw_post_render(self.request)
    
async def raw_get_render(request):
    url = request.query.get("url")
    print(url)
    # page = await browser.newPage()
    return web.Response(text='1')


async def raw_post_render(request):
    params = await request.json()
    url = params.get('url')
    if not url:
        pass
    return web.Response(text=url)
