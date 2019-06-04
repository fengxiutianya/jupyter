#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:55
    filename    : crawlerbaidu2.py
    info        : 使用异步方式改写爬取百度
'''
import socket
from selectors import DefaultSelector, EVENT_WRITE

selector = DefaultSelector()

sock = socket.socket()
sock.setblocking(False)

try:
    sock.connect(("www.baidu.com",80))
except BlockingIOError:
    pass

def connected():
    selector.unregister(sock.fileno())
    print("connected")
'''
    连接主要过程
'''
selector.register(sock.fileno(),EVENT_WRITE,connected)

class Future:
    def __init__(self):
        self.result =None
        self.__callbacks=[]

    def add_done_callback(self,fn):
        self.__callbacks.append(fn)

    def set_result(self,result):
        self.result = result
        for callback in self.__callbacks:
            callback(self)

class AsyncRequest:
    def __init__(self,host,url,port,timeout=5):
        self.sock = socket.socket()
        self.sock.settimeout(timeout)
        self.sock.setblocking(False)

        self.host = host
        self.url = url
        self.port = port
        self.method = None

    def get(self):
        self.method = "GET"
        self.request = '{} {} HTTP/1.0\r\nHost: {}\r\n\r\n'.format(self.method, self.url, self.host)
        return self

    def process(self):
        if self.method is None:
            self.get()
        try:
            self.sock.connect((self.host,self.port))
        except BlockingIOError:
            pass
        self.f = Future()
        selector.register(self.sock.fileno(),EVENT_WRITE,self.on_connected)
        yield  self.f
        selector.unregister(self.sock.fileno())
        self.sock.setblocking(self.request.encode('ascii'))

    def on_connected(self, key, mask):
        self.f.set_result(None)