#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: app.py

@time: 2018/5/17 下午6:18
"""
import asyncio
from aiohttp import web
import uvloop
from aiohttp_swagger import setup_swagger
from core.main import chromium_manager
from server.views.render import raw_get_render, raw_post_render, RenderView

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def healthz(request):
    """
        ---
        description: app healthz check
        tags:
        - Health check
        produces:
        - text/plain
        responses:
            "200":
                description: successful operation. Return "Healthz Checked!" text
            "405":
                description: invalid HTTP Method
    """
    return web.Response(text='Healthz Checked!')


async def index(request):
    """
        ---
        description: home
        tags:
        - Index
        produces:
        - text/plain
        responses:
            "200":
                description: 欢迎！
            "405":
                description: invalid HTTP Method
    """
    return web.Response(text='欢迎!')

async def redirect(request):
    raise web.HTTPFound('/')

    

async def get_liveness_nodes(request):
    """获取所有存活节点"""
    """
    Planed at v1.0
    """
    pass


def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/healthz', healthz)
    app.router.add_get('/redirect', redirect)
    app.router.add_view('/render', RenderView)

def setup_browser():
    print('setup_browser start')
    loop = asyncio.get_event_loop()
    loop.run_until_complete(chromium_manager.setup())
    print('setup_browser end')

def create_app(loop=None):
    app = web.Application(loop=loop)
    setup_routes(app)
    setup_browser()
    setup_swagger(app)
    web.run_app(app, host='0.0.0.0', port=9999)

    
    
if __name__ == '__main__':
    create_app()