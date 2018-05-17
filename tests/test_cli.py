#!/usr/bin/env python
# encoding: utf-8
"""

@author:nikan

@file: test_cli.py

@time: 2018/5/17 下午10:48
"""

from aiohttp import web

from server.app import setup_routes


def create_test_app(loop=None):
    app = web.Application(loop=loop)
    setup_routes(app)
    return app


async def test_index(test_client):
    client = await test_client(create_test_app)
    resp = await client.get('/')
    assert resp.status == 200
    text = await resp.text()
    assert '欢迎!' in text


async def test_healthz(test_client):
    client = await test_client(create_test_app)
    resp = await client.get('/healthz')
    assert resp.status == 200
    text = await resp.text()
    assert 'Healthz Checked!' in text
    
    
async def test_raw_post_render(test_client):
    client = await test_client(create_test_app)
    resp = await client.post('/raw_post_render', json={
        'url': 'https://www.baidu.com/'
    })
    assert resp.status == 200
    text = await resp.text()
    assert 'https://www.baidu.com/' in text
    
    resp = await client.post('/raw_post_render', json={
    
    })
    assert resp.status == 200
    text = await resp.text()
    assert 'https://www.baidu.com/' in text