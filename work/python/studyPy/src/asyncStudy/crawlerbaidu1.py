#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:50
    filename    : crawlerbaidu1.py
    info        : 同步方式抓取百度
'''
import socket


def sync_way():
    ### socket的建立连接-接收过程都是一个一个来的，在没完成一个连接时不能进行其他连接的处理。
    for i in range(100):
        ### 这一部分需要时间
        sock = socket.socket()
        sock.connect(('www.baidu.com', 80))
        print('connected')
        request = 'GET {} HTTP/1.0\r\nHost: www.baidu.com\r\n\r\n'.format('/s?wd={}'.format(i))
        ### 这一步需要时间
        sock.send(request.encode('ascii'))
        response = b''
        ### 这一部分十足赛式的，需要时间
        chunk = sock.recv(4096)
        while chunk:
            response += chunk
            chunk = sock.recv(4096)
        print('done!!')

from time import time
start = time()

sync_way()

end = time()
print ('Cost {} seconds'.format(end - start))
## Cost 61.54423499107361 seconds