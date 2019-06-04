#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
    author      : zhangke
    createTime  : 2019-01-23 11:23
    filename    : crawlerDouban5.py
    info        : 由于GIL的存在， 多进程的方式调用
'''
import requests
from lxml import etree
from time import time
from concurrent.futures import ProcessPoolExecutor

url = 'https://movie.douban.com/top250'

def fetch_page(url):
    response = requests.get(url)
    return response

def fetch_content(url):
    response = fetch_page(url)
    page = response.content
    return page

def parse(url):
    page = fetch_content(url)
    html = etree.HTML(page)

    xpath_movie = '//*[@id="content"]/div/div[1]/ol/li'
    xpath_title = './/span[@class="title"]'
    xpath_pages = '//*[@id="content"]/div/div[1]/div[2]/a'

    pages = html.xpath(xpath_pages)
    fetch_list = []
    result = []
    for element_movie in html.xpath(xpath_movie):
        result.append(element_movie)

    for p in pages:
        fetch_list.append(url + p.get('href'))
    with ProcessPoolExecutor(max_workers=4) as executor:
            for page in executor.map(fetch_content,fetch_list):
                html = etree.HTML(page)
                for element_movie in html.xpath(xpath_movie):
                    result.append(element_movie)
    for i, movie in enumerate(result, 1):
        title = movie.find(xpath_title).text
if __name__=='__main__':
    from time import time
    start = time()
    for i in range(5):
        parse(url)
    end = time()
    print('Cost {} seconds'.format((end - start) / 5))
## Cost 2.06529541015625 seconds