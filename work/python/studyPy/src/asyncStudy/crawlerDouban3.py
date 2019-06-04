#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:17
    filename    : crawlerDouban3.py
    info        : 将xml替换成标准的re库
'''
import requests
from time import time
import re

url = 'https://movie.douban.com/top250'


def fetch_page(url):
    response = requests.get(url)
    return response


def parse(url):
    response = fetch_page(url)
    page = response.content

    fetch_list = set()
    result = []

    for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
        result.append(title)

    for postfix in re.findall(rb'<a href="(\?start=.*?)"', page):
        fetch_list.add(url + postfix.decode())

    for url in fetch_list:
        response = fetch_page(url)
        page = response.content
        for title in re.findall(rb'<a href=.*\s.*<span class="title">(.*)</span>', page):
            result.append(title)

    for i, title in enumerate(result, 1):
        title = title.decode()
        # print(i, title)
if __name__=='__main__':
    from time import time
    start = time()
    for i in range(5):
        parse(url)
    end = time()
    print('Cost {} seconds'.format((end - start) / 5))
### Cost 3.238160181045532 seconds